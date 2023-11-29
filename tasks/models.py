import datetime
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    # TODO: need to prevent title from being any defualt filter option ie
    # none, incomplete
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def count(self, user):
        self.count = Task.objects.filter(user=user, tag=self.pk).count()
        return self.count


class Task(models.Model):
    # cascade if user deleted, will deleted its tasks
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks"
    )
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    due = models.DateField(auto_now_add=False, null=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def days_since_creation(self):
        return self.created >= datetime.date.today() - datetime.timedelta(days=1)

    def days_away_from_due(self):
        if self.due is not None:
            today = datetime.date.today()
            due = self.due
            delta = due - today
            return delta.days
        else:
            return None

    # Model metadata is “anything that’s not a field”,
    # such as ordering options (like i.e. sorting),
    # database table name (db_table),
    # or human-readable singular and plural names
    class Meta:
        ordering = ["complete"]
        # ffr filtering
        # Index(Lower("title").desc(), "pub_date", name="lower_title_date_idx")
        ## creates an index on the lowercased value of the title field in descending order and the pub_date field in the default ascending order.
