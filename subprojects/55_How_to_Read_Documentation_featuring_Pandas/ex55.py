# Step 1 with Pandas
# Let's go through the Pandas documentation and answer each of these questions:
# Yes, it looks like the documentation is the right version.
# The /docs/ has both guides and API reference. You'll need the guide to follow,
# and the API reference to look up specifics about things you use in your own
# projects later.
# Yes, there's both getting started tutorials which show you how to do various
# things, and a cookbook in the User guide with many quick examples.
# What are the most interesting topics to you? In this exercise you'll focus on
# DataFrame so any documents that cover that are useful. If you wanted to process
# many .csv files then you'd look for documents explaining loading and saving
# .csv files.

# Step 2: Determine Your Strategy
# What do you do if most of these have "No" answers? What if the project only has
# auto-generated API docs and not a single document or example explaining how to
# use the API? First, do you have to use this pile of garbage? Life's too short to
# use software that not even the developers care about, so maybe just don't use it.
# If you really want to use it or have to use it, then you have two complimentary
# strategies:
# Find guides and example code other people wrote about the project.
# Choose your own small project that will use this project, and spend your time
# reading the API docs to get your project working.
# If the project has everything you need then you have a couple different strategies:
# Start with any cookbooks and how-to documents with many examples.
# Start with the guides that walk through each topic the project thinks is important.
# Start with the API docs anyway and try to make your own software using the API.
# These options are not mutually exclusive. Start with one option, and if it's not
# working, switch to another. Keep doing this until you understand enough to use
# the project or study further.

# Step 2 with Pandas
# In the Pandas example we have everything we need except an overall curriculum
# telling us where to go, so that's why you need a strategy. I have three
# complimentary strategies in this situation:
# Start with the cookbooks and how-to documents and use those as a guide to dive
# deeper into related documentation.
# Start with the deeper user guide and as you go through it read cookbooks and
# how-to documents to get practical examples.
# Try to make something using the API reference. Sometimes this is the best strategy
# if you are hot to work on an idea, but don't get discouraged if it's too hard. If
# you get stuck, switch to the other strategies.

# Step 3: Code First, Docs Second
# This will seem counter-intuitive but when reading programmer documentation you
# will have more success if you start with the code, then read about it. This works
# because the code is something you can experience and that experience gives you
# better understanding of what's being said in the documentation.

# Step 3 with Pandas
# Let's look at the 10 minute guide to Pandas as an example. Right away there's
# this code:
import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# this prints it in Jupyter
s
dates = pd.date_range("20130101", periods=6)
# print it in Jupyter
dates
# This code is spread across multiple short descriptions about the code, so you
# type each example in first. Once it's working, change it around and then read
# the descriptions. This will make the descriptions easier to understand.
# However, if you read the descriptions first this is what you read:
# Customarily, we import as follows.
# Creating a Series by passing a list of values, letting
# pandas create a default RangeIndex.
# Creating a DataFrame by passing a NumPy array with a
# datetime index using date_range() and labeled columns:
# Those on their own or with a quick glance at the code make almost no sense. After
# you get the code working these sentences help fill in gaps in your understanding.
# They also link to more documentation on what you just used.

# Step 4: Break or Change the Code
# After you get a piece of code working take the time to break it so you can see
# how errors are handled. One massive blocker for beginners is deciphering the
# convoluted error messages programming languages produce. There's almost a weird
# art to reading them and using Google to find the answer. One of the ways to learn
# the "language of terrible errors" is to expose yourself to as many errors as
# possible on purpose so you can study them.
# The second thing to do is ask if you can do something and then try to do it. You'll
# ask, "How do I give a Series a different index?" Or, you might ask, "How can I
# pass a Series to a DataFrame?" The kinds of changes you want to focus on are
# combinations of things you just learned.

# Step 5: Take Notes
# A key aspect of learning to code (or anything) is explaining what you've learned
# back to yourself. The best way to do this while you're working is to have a
# notes.txt file in the directory where you're putting the code you write. In this
# notes.txt write down questions you have, things you discover, and comments about
# what you're learning.
# Another important part of the notes.txt is links. You should be recording links to
# what you read or what you need to read as you work. This will help you later when
# you need to remember where you read about something.

# Step 6: Use it On Your Own
# The entire purpose of this last module is to move you from someone who knows Python
# to someone who can use Python to express their own ideas. After you feel you have
# enough understanding of the project you should try to make something of any size
# with it. This is when you will switch to relying more on API reference than the
# other documentation.

# Step 6 with Pandas
# If you're stuck and can't think of anything to create, then take an example from
# the cookbook or how-to documents documentation and modify it to do something new.
# Maybe you have it load the data from a SQL database or change the data used.

# Step 7: Write About What You Learned
# When I think of painting, writing, and programming I think of them as mediums for
# articulating my automatic thoughts, experiences, and feelings so I can consciously
# understand them. Painting helps me understand what I see. Writing helps me understand
# what I know and feel. Programming helps me understand how to do something.
# I spend all day using my eyes to see the world, but it's only when I try to paint what
# I see that I start to consciously understand what I'm seeing. Painting forces me to
# consciously understand the automatic way my visual system processes the world.
# Programming forces me to structure my understanding of how something works into logical
# steps and structures. After I turn a process or idea into code I understand how it
# could actually work.
# Writing helps me organize my almost random thoughts into a coherent conscious structure.
# The act of organizing all of my thoughts into an essay that makes sense and flows naturally
# helps me further understand my ideas.
# More importantly, each of these mediums--painting, programming, and prose--force me to
# explore what I don't know. Externalizing my knowledge in these ways gives me a glimpse
# into my brain. I can look at a painting and say, "Well it looks like I have no idea what
# this flower actually looks like." I can study code and see, "I clearly have no idea how
# this algorithm is supposed to work." I can read through an essay and see, "I really don't
# know how to explain what I'm feeling about this topic."
# This is why you should write about what you've learned. You don't have to show it to
# anyone or be a good writer. Your writing doesn't have to be original. I'll tell you, 99%
# of all writing is not original. The point is not to impress other people with how clever
# a writer you are. The point is to explain to yourself what you know so you can see if you
# actually learned something.

# Step 7 with Pandas
# For Step 7 I want you to write at least 8-10 paragraphs teaching someone else what you've
# just learned about DataFrames. How would you explain the DataFrame to someone who knows
# Python? What is your best advice on how to use it? Are there any things to avoid when using
# it?
# Another option is to write your own curriculum to learn the Pandas DataFrame. If you were to
# write a curriculum for someone else what links should they read in order to best understand
# it. For each link describe what they learn at that stage, and how it relates to the previous
# link they studied.
# A final option is to use Jupyter to create a Notebook that demonstrates and explains
# everything someone else would need to learn. I suggest first write a short version of the
# curriculum idea, and then turn that into a structured notebook that follows the curriculum.

# Step 8: What's the Gestalt?
# The final step in this process is to ask yourself, "What's the big picture for this project?"
# This is a more abstract step and should fall out naturally from your writings and notes, but
# being able to summarize the project will give you a mental framework to hold everything else
# you learn.
# Your understanding of the project might be different from the authors, but your description
# of the project is more for you than a general statement for everyone.

# Step 8 with Pandas
# If I were to summarize the purpose of Pandas I might have several "gestalt statements":
# "Pandas' purpose is to provide Python with higher level features commonly found in other
# statistics and math languages like R, SAS, and Mathematica."
# "Pandas gives an easier way to load, structure, and manipulate tabular data for analysis."