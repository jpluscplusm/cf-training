require "sinatra"
require "sinatra/json"

class App < Sinatra::Base
  get '/' do
    status 200
    content_type "application/json"

    body = { :message => "Hello, world!" }

    json body
  end
end
