import datetime
from google.appengine.api import mail

from handlers.base import BaseHandler
from models.topic import Topic
from models.subscribe_to_forum import SubscriberToForum


class SubscribeToForumCron(BaseHandler):
    def get(self):
        dt_send_to = datetime.datetime.now() - datetime.timedelta(hours=24)
        hottest_topics = Topic.query(Topic.created <= dt_send_to).fetch()
        subscribers_to_forum = SubscriberToForum.query().fetch()

        s = ","
        joined_topics = s.join(hottest_topics)

        for email in subscribers_to_forum:
            mail.send_mail(
                sender="luckie.luke@gmail.com",
                to= email,
                subject="Here are our hottest topics:",
                body="""Topics with title %s have been created in last 24 hours

                    <a href='/topic-details/'>Link to the forum</a>"""
                     % joined_topics
            )
