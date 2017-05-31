import os
import unittest
import webapp2
import webtest
import uuid

from google.appengine.ext import testbed


from main import MainHandler
from handlers.topics import TopicDetailsHandler
from models.topic import Topic


class TopicDetailsTests(unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication(
            [
                webapp2.Route('/topic/<topic_id:\d+>', TopicDetailsHandler),
            ])

        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        """ Uncomment the stubs that you need to run tests. """
        self.testbed.init_datastore_v3_stub()
        # self.testbed.init_memcache_stub()
        # self.testbed.init_mail_stub()
        # self.testbed.init_taskqueue_stub()
        self.testbed.init_user_stub()
        # ...

        """ Uncomment if you need user (Google Login) and if this user needs to be admin. """
        os.environ['USER_EMAIL'] = 'some.user@example.com'
        # os.environ['USER_IS_ADMIN'] = '1'

    def tearDown(self):
        self.testbed.deactivate()

    def test_topic_details_handler(self):
        topic = Topic(title="Test topic", content="Random text content", author_email="luckie.luke@gmail.com")
        topic.put()

        get_response = self.testapp.get('/topic/{}'.format(topic.key.id()))
        self.assertEqual(get_response.status_int, 200)
