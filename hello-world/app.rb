require "sinatra"
require "sinatra/json"

STOCK_MAX = ENV.fetch('STOCK_MAX_INT')

class App < Sinatra::Base
  get '/p/:pCode' do |pCode|
    status 200
    content_type "application/json"

    stock_level = Random.rand(STOCK_MAX.to_i)
    body = { :product => pCode, :stock => stock_level }

    json body
  end
end
