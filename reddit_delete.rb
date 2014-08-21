require 'redditkit'

USERNAME = "XXXXXXXXX"
PASSWORD = "XXXXXXXXX"

authenticated_client = RedditKit::Client.new USERNAME, PASSWORD

comments = authenticated_client.my_content :category => :comments, :limit => 100

comments.each do |comment|
  authenticated_client.delete comment
end
