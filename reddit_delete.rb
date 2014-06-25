require 'snooby'

USERNAME = "xxxxx"
PASSWORD = "xxxxx"

reddit = Snooby::Client.new('me, v1.0')
reddit.authorize!(USERNAME, PASSWORD)

comments = reddit.user(USERNAME).comments(1000)

comments.each do |comment|
	comment.delete
end

##
