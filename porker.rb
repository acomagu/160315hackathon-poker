#!/usr/bin/env ruby
# -*- coding: utf-8 -*-
# vim:set fileencoding=utf-8:
require 'net/http'
require 'open-uri'

mykey = "46e6b984-7166-4dd8-a763-52408278a852"

def dumb_poker_player(mykey)
    # Infinite Loop
    while true 
      
        # Your client should sleep 1 second.
        # If you send too many requests at once, we will start throttling your requests.
        # This will cause you to reach the timeout limit which will cause your player to FOLD.
        sleep 1
    
        # GET request.
        # Ask the server "What is going on?"
        response = game_state(mykey)
    
        # Parse the response so you can use the data.
        turn_data = JSON.parse(response.body)
        
        # Logic!!
        # This logic is boring. But, yours should be more epic!
        if turn_data["your_turn"]
            action = params = discards = nil
      
            # Is it a betting round, but not the river? Let's always call.
            if  turn_data["betting_phase"] == "deal" ||
                turn_data["betting_phase"] == "flop" ||
                turn_data["betting_phase"] == "turn"
                action = "call"
                params = nil
                        
            # Is it the river phase? Always bet 10 more.
            elsif turn_data["betting_phase"] == "river"
                action = "bet"
                params = 10
            end
        
            # Stores all your parameters in a single variable
            my_action = {:action_name => action, :amount => params}
          
            # POST a request to the server
            response = player_action(mykey, my_action)
        end
    end
end

# GET
def game_state(key)
    # a get request to http://nolimitcodeem.com/api/players/:key
    url = URI.parse('http://nolimitcodeem.com/api/players/:key')
    body = open(url, &:read)
    # res = Net::HTTP.start(url.host, url.port) do |http|
    #     http.get('/index.html')
    # end
end

# POST
def player_action(key, params)
  # do a post request to http://nolimitcodeem.com/api/players/:key/action
end

game_state(mykey)
