import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'imdb'

    start_urls = [
        'https://www.imdb.com/chart/top/?ref_=nv_td_mv250',
    ]

    def parse(self, response):

        rows = response.css('table.chart.full-width tbody tr')

        for row in rows:
            name = row.css('td.titleColumn a::text').get()
            year = row.css('td span::text').get()
            rating = row.css('td strong::text').get()

            yield {
                'movieName' : name,
                'released' : year,
                'rating' : rating
            }

        