import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author' #spider name
    start_urls = ['http://quotes.toscrape.com/]

    def parse(self, response): # create a parse function
        # follow links to author pages
        authorElements = response.css('.author + a::attr(href)')
        for href in authorElements
            yield response.follow(href, self.parse_author)
        
        # follow the pagination link
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)
    
    def parse_author(self, response): # create a parser function to parse the author
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }