# What's the most efficient way to write tests then? I've found this 
# process to provide the most value for the least effort:

# Write tests that pretend to be the user, whether that user is someone 
# accessing your website or a programmer using your API. Your tests 
# should pretend to be an actual person doing good and bad things.

# Cause as many errors as possible and confirm they are actually reported. 
# For example, on a registration form give bad email addresses, usernames, 
# and passwords then check for the errors. If your tests run later and you 
# have no errors then you broke something for sure.

# Use a coverage reporting tool to confirm that your tests are at a 
# minimum hitting most of the code, including error handlers.

# Any code you can't hit should be analyzed and either removed as useless 
# or get separate tests if it's actually not useless. If you can't hit the 
# code from the UI then why is it in there? Just in case? Just in case code 
# is a security time bomb so just remove it. You can always bring it back 
# later. If it's code that's run in a background job or simply not used by 
# the user, then write a special test just for that code.

# Finally, if your code uses any other services run by other people then 
# write tests that confirm those services keep working. You won't believe 
# how often companies and people change their services without telling you. 
# A test that checks their service can save you significant downtime in the 
# future. The only problem with these tests is you typically can't run them 
# in a usual developer workflow. It's better to run this separately in a 
# monitoring tool or some other infrequent checking service. If your tests 
# run service checks you may take the service down--or worse--incur massive 
# costs as you rack up thousands of requests a day on accident.

# If you're working by yourself you can get away with just steps 1-3, but 
# as your code grows you'll need to start doing the rest of these. These 
# also aren't an exhaustive list of things you need to do when testing 
# software. That's an entire book on its own.

class Person:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def hit(self, who):
        who.hp -= self.damage

    def alive(self):
        return self.hp > 0