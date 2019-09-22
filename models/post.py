import uuid
import datetime
from database import Database

class Post(object):
  
  """This is a blog post CLASS"""
  """Parameters default value """

  def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
    self.blog_id = blog_id
    self.title = title
    self.content = content
    self.author = author
    self.created_date = date
    # Generate random ID using uuid
    self.id = uuid.uuid4().hex if id is None else id
  
  """Connecting and saving to MongoDB"""

  def save_to_mongo(self):
    Database.insert(collection='posts', data=self.json())

  """Collection for post"""
  def json(self):
    return {
      'id': self.id,
      'title': self.title,
      'blog_id': self.blog_id,
      'content': self.content,
      'author': self.author,
      'created_date': self.created_date
    }

  @staticmethod
  def from_mongo(id):
    return Database.find_one(collection='posts', query={'id': id})

  @staticmethod
  def from_blog(id):
    return [post for post in Database.find(collection='posts', query={'blog_id': id})]