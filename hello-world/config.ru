require "bundler/setup"
require "./app"

app = Rack::Builder.app do
  run App
end

run app
