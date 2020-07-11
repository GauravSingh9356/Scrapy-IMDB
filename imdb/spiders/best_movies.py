# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = [
        'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths='//h3[@class="lister-item-header"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths='//a[@class="lister-page-next next-page"][1]'))
    )

    def parse_item(self, response):
        yield{
            'title': response.xpath('//div[@class="title_wrapper"]/h1/text()').get(),
            'year_release': response.xpath('//span[@id="titleYear"]/a/text()').get(),
            'duration': response.xpath('normalize-space(//time[1]/text())').get(),
            'genre': response.xpath('//div[@class="subtext"]/a[1]/text()').get(),
            'rating': response.xpath('//span[@itemprop="ratingValue"]/text()').get(),
            'movie_url': response.url,

        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
