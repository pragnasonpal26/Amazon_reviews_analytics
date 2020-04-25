# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    allowed_domains = ['amazon.com']
    myBaseUrl = "https://www.amazon.com/All-New-Amazon-Echo-Dot-Add-Alexa-To-Any-Room/product-reviews/B01DFKC2SO/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls = []
    
    for i in range(1,100000):
        start_urls.append(myBaseUrl+str(i))
    
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
             
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
             
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
             
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1

    
