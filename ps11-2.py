#   _________.___   ___________    ________     __________  _________  ____ ____
#  /   _____/|   | /_   \   _  \  /  _____/     \______   \/   _____/ /_   /_   |
#  \_____  \ |   |  |   /  /_\  \/   __  \       |     ___/\_____  \   |   ||   |
#  /        \|   |  |   \  \_/   \  |__\  \      |    |    /        \  |   ||   |
# /_______  /|___|  |___|\_____  /\_____  / /\   |____|   /_______  /  |___||___|
#         \/                   \/       \/  )/                    \/
#
# NOTE: This project requires using the Facebook API. If you do not have a Facebook account
# or would prefer not to use your personal account for this project, please create a new
# account.

import json
import webbrowser
import unittest
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix



# Fill in the credentials you get from registering a new application
APP_ID     = '<put your app id here>'
APP_SECRET = '<put your app secret here>'
facebook_session = False

# Reference: https://requests-oauthlib.readthedocs.io/en/latest/examples/facebook.html
def makeFacebookRequest(baseURL, params = {}):
    global facebook_session
    if not facebook_session:
        # OAuth endpoints given in the Facebook API documentation
        authorization_base_url = 'https://www.facebook.com/dialog/oauth'
        token_url = 'https://graph.facebook.com/oauth/access_token'
        redirect_uri = 'https://www.programsinformationpeople.org/runestone/oauth'

        scope = ['user_posts','pages_messaging','user_managed_groups','user_status','user_likes']
        facebook = OAuth2Session(APP_ID, redirect_uri=redirect_uri, scope=scope)
        facebook_session = facebook_compliance_fix(facebook)

        authorization_url, state = facebook_session.authorization_url(authorization_base_url)
        print('Opening browser to {} for authorization'.format(authorization_url))
        webbrowser.open(authorization_url)

        redirect_response = raw_input('Paste the full redirect URL here: ')
        facebook_session.fetch_token(token_url, client_secret=APP_SECRET, authorization_response=redirect_response.strip())

    return facebook_session.get(baseURL, params=params)

# PROBLEM 1: Fill in the APP_ID and APP_SECRET variables above and make a request
# to the Facebook Graph API at: https://graph.facebook.com/me. Using json.loads, store the parsed result
# in the variable current_user. It should have keys 'name' and 'id'
#
# To get an App ID and App Secret, you will need to register for a new Facebook application at https://developers.facebook.com. To do this:
#   1. Go to https://developers.facebook.com > Get Started
#   2. Accept platform and privacy policies
#   3. Create App ID
#   4. Choose an App display name and select a category for your app (it can be any category)
#   5. Now that your app is registered, go to Dashboard to get your App ID and App Secret
#
# You just need to do one more thing before your app is ready to go. Do the following:
#   1. On the web page for your app, go to Settings (in the left panel)
#   2. At the bottom of the settings page, click "+ Add Platform"
#   3. Select Website as the platform
#   4. Copy and paste this URL into the "Site URL" box: https://www.programsinformationpeople.org/runestone/oauth
#   5. Click "Save Changes" (bottom right of screen)
#   6. On the same page, scroll up to where it says "App Domains"
#   7. Copy and paste this URL into the "App Domains" box: https://www.programsinformationpeople.org
#   8. Click "Save Changes" again

# TODO: make a call to makeFacebookRequest

# This code makes lists of positive words and negative words, saving them in the variables pos_ws and neg_ws.
# DO NOT CHANGE THIS CODE, you'll need it later in the PSet.
pos_ws = []
f = open('positive-words.txt', 'r')

for l in f.readlines()[35:]:
    pos_ws.append(unicode(l.strip()))
f.close()

neg_ws = []
f = open('negative-words.txt', 'r')
for l in f.readlines()[35:]:
    neg_ws.append(unicode(l.strip()))

# PROBLEM 2:
# Fill in the definition of the class Post to hold information about one post that you've made on Facebook.
# Add to the __init__ method additional code to set the instance variables comments and likes.
# More instructions about that follow, in the code below.
# You need to pull out the appropriate data from the json representation of a single post.
# You can find a sample in the file samplepost.json.
# There are tests that check whether you've pulled out the right data.

class Post():
    """object representing status update"""
    def __init__(self, post_dict={}):
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = ""
        # [PROBLEM 2A] if the post dictionary has a 'comments' key, set an instance variable self.comments
        # to the list of comment dictionaries you extract from post_dict. Otherwise, set self.comments to be an empty list: []

        # Something similar has already been done for the contents (message) of the original post, which is the value of the 'message' key in the dictionary, when it is present (photo posts don't have a message). See above.

        # Extracting the list of comment dictionaries from a post_dict is a little harder. Take a look at the sample of what a post_dict looks like in the file samplepost.txt to figure out where to find the right information.

        # [PROBLEM 2B] Now, similarly, if the post has any likes, set self.likes to the value of the list of likes dictionaries. Otherwise, if there are no 'likes', set self.likes to an empty list.


    # PROBLEM 3: In the Post class, fill in three methods:
    # -- positive() returns the number of words in the message that are in the list of positive words called pos_ws (provided in our code)
    # -- negative() returns the number of words in the message that are in the list of negative words called neg_ws (provided in our code)
    # -- emo_score returns an integer: the difference between positive and negative scores
    # The beginnings of these functions are below -- fill in the rest of the method code! There are tests of these methods later on.

    def positive(self):
        return None

    def negative(self):
        return None

    def emo_score(self):
        return None

# PROBLEM 4: Add comments for these lines of code explaining what is happening in them.
sample = open('samplepost.json').read()
sample_post_dict = json.loads(sample)
p = Post(sample_post_dict)

# Use the next lines of code if you're having trouble getting the tests to pass. They will help you understand what a post_dict contains, and what your code has actually extracted from it and assigned to the comments and likes instance variables.
#print(json.dumps(sample_post_dict, indent=4))
#print(json.dumps(p.comments, indent=4))
#print(json.dumps(p.likes, indent=4))


# Now, get a json-formatted version of your last 100 posts on Facebook.
# (Don't worry if you don't have any feed posts; still write the code to make a request to get your feed.)
baseurl = 'https://graph.facebook.com/me/feed'


# PROBLEM 5: Use a list comprehension to create the list of Post instances.
#       You may EITHER choose to use the data you get from Problem 4 ('https://graph.facebook.com/me/feed')
#               OR use the data from group_106_feed.json (in which case, you'll want to uncomment the code below)

# sample_feed = json.loads(open('group_106_feed.json').read())

# For each of those posts in the feed you get back,
    # -- create an instance of your class Post.
    # Save all the post instances in a list called post_insts.
    # If you passed the tests above, all this should work just fine if you create one instance per post and save them all in a list, using a list comprehension structure.
    # This requires understanding -- but not very many lines of code!


# TODO: Write code to do that here



# PROBLEM 6:
# Write code to compute the top 3 likers and the top 3 commenters on your posts overall, and save them in lists called top_likers and top_commenters. So top_likers should contain 3 names of people who made the most likes on all your Facebook posts, and top_commenters should contain 3 names of people who made the most comments on all your Facebook posts.
# HINT: creating dictionaries and sorting may both be useful here!

### Code to help test whether problem 6 is working correctly
try:
    print "Top commenters:"
    print top_commenters
    for i in range(len(top_commenters)):
        print(i, top_commenters[i])

    print "Top likers:"
    print top_likers
    for i in range(len(top_likers)):
        print(i, top_likers[i])
except:
    print "Problem 6 not correct.\ntop_commenters and/or top_likers has not been defined or is not the correct type, or you have another error."


# PROBLEM 7: Write code to output a .csv file called emo_scores.csv that lets you
# make scatterplots (in Excel or Google sheets) showing net positivity (emo_scores)
# on x-axis and comment-counts and like-counts on the y-axis.
# Each row should represent one post, and should include: emo score, comment counts,
# and like counts, in that order.


# Post a screenshot of your scatterplot to our facebook group!

# You can see what the scatterplot might look like
# in emo_scores.xlsx, included in the assignment. (In the example case, there's not
# an obvious correlation between positivity and how many comments or likes. There
# may not be, but you find that out by exploring the data!)


# Can you see any trends or possible relationships between likes, comments, and emo_scores? (Something to consider. Not graded.)

# When you're finished, upload this file to Canvas.
# TODO: On canvas, ONLY SUBMIT THIS FILE (no other files in the directory)

# PROBLEM 8: Which project do you plan on doing for your final project?
# TODO: let us know which final project you plan on doing.

############################################################
##                                                        ##
##          DO NOT MODIFY THE TEST CODE BELOW             ##
##             WE USE IT TO TEST YOUR CODE                ##
##                                                        ##
############################################################
class Problem3(unittest.TestCase):
    def test_instvar_1(self):
        self.assertEqual(type(p.comments), type([]), "testing type of p.comments")
    def test_instvar_2(self):
        self.assertEqual(len(p.comments), 4, "testing length of p.comments")
    def test_instvar_3(self):
        self.assertEqual(type(p.comments[0]), type({}), "testing type of p.comments[0]")
    def test_instvar_4(self):
        self.assertEqual(type(p.likes), type([]), "testing type of p.likes")
    def test_instvar_5(self):
        self.assertEqual(len(p.likes), 4, "testing length of p.likes")
    def test_instvar_6(self):
        self.assertEqual(type(p.likes[0]), type({}), "testing type of p.likes[0]")
    def test_method_1(self):
        sample = open('samplepost.json').read()
        sample_post_dict = json.loads(sample)
        p = Post(sample_post_dict)
        p.message = "adaptive acumen abuses acerbic aches for everyone"
        self.assertEqual(p.positive(), 2, "testing return value of .positive()")
        self.assertEqual(p.negative(), 3, "testing return value of .negative()")
        self.assertEqual(p.emo_score(), -1, "testing return value of .emo_score()")

class Problem6(unittest.TestCase):
    def test_1(self):
        self.assertEqual(type(top_likers[1]),type(u""), "Testing that elements of top_likers are Unicode strings (they should be strings of the likers' names -- note that you'll have to judge whether they're the correct names)")

if __name__ == '__main__':
    unittest.main(verbosity=2)

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMM             MMMMMMMMMMMMMMMMM             MMMMMMMMM
#MMMMMMM              MMMMMMMMMMMMMMM              MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMM                 MMMMMMMMM                 MMMMMMMMM
#MMMMMMM                  MMMMMMM                  MMMMMMMMM
#MMMMMMMMMMM               MMMMM                MMMMMMMMMMMM
#MMMMMMMMMMM                MMM                 MMMMMMMMMMMM
#MMMMMMMMMMM                 V                  MMMMMMMMMMMM
#MMMMMMMMMMM                                    MMMMMMMMMMMM
#MMMMMMMMMMM         ^               ^          MMMMMMMMMMMM
#MMMMMMMMMMM         MM             MM          MMMMMMMMMMMM
#MMMMMMMMMMM         MMMM         MMMM          MMMMMMMMMMMM
#MMMMMMMMMMM         MMMMM       MMMMM          MMMMMMMMMMMM
#MMMMMMMMMMM         MMMMMM     MMMMMM          MMMMMMMMMMMM
#MMMMMMM                MMMM   MMMM                MMMMMMMMM
#MMMMMMM                MMMMMVMMMMM                MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMM/-------------------------/MMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMM/- SCHOOL OF INFORMATION -/MMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMM/-------------------------/MMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
