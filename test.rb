#!/usr/bin/env ruby
# -*- coding: utf-8 -*-
# vim:set fileencoding=utf-8:

# require 'net/http'
# require 'url'

# url = URI.parse('http://nolimitcodeem.com/api/players/46e6b984-7166-4dd8-a763-52408278a852/')
# res = Net::HTTP.start(url.host, url.port) do |http|
#     http.get('/index.html')
# end

require "open-uri"

key = "name"
# 100.times do
# body = open("http://nolimitcodeem.com/api/players/46e6b984-7166-4dd8-a763-52408278a852/name", &:read)
body = open("http://nolimitcodeem.com/api/players/46e6b984-7166-4dd8-a763-52408278a852/name", &:get)
# endhttp://nolimitcodeem.com/api/players/:key
p body
