from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Skill(models.Model):
    # Filter categories shown on the website
    SKILL_TYPES = (
        ('language', 'Languages'),
        ('framework', 'Frameworks'),
        ('tool', 'Tools & Platforms'),
    )
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES, default='language')
    # Full icon class, e.g. "devicon-python-plain colored"
    icon_name = models.CharField(max_length=80, default='bi bi-code-slash')
    # You will write this text yourself from Django Admin
    description = models.TextField(blank=True)
    # Smaller number = shown earlier
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.name    

class Experience(models.Model):
    KIND_CHOICES = (
        ('internship', 'Internship'),
        ('training', 'Summer Training'),
    )
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='internship')
    role = models.CharField(max_length=120)
    institution = models.CharField(max_length=150)          # company name
    location = models.CharField(max_length=100, blank=True)  # e.g. Remote / India
    period = models.CharField(max_length=50)                 # e.g. Nov 2026 (Ongoing)
    description = models.TextField(blank=True)
    # One point per line, shown as "Key Contributions"
    contributions = models.TextField(blank=True, help_text="One point per line")
    tech_stack = models.CharField(max_length=200, blank=True, help_text="Comma separated, e.g. Python, Django")
    # Smaller number = shown first (newest entry should be 1)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.role} - {self.institution}"

    def get_contribution_list(self):
        # Turn the text box into a list, ignoring empty lines
        return [line.strip() for line in self.contributions.splitlines() if line.strip()]

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]    
    
class Project(models.Model):
    # Short, simple values (no slashes or typos) so filter buttons can match them
    CATEGORY_CHOICES = [
        ('fullstack', 'Full Stack'),
        ('frontend', 'Web / Frontend'),
    ]

    title = models.CharField(max_length=150)
    # Default must be one of the choices above (it was 'backend' before, which was invalid)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='fullstack')
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, help_text="Commas se alag karein, jaise: Python, Django, PostgreSQL")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="Agar direct image link ho jaise Cloudinary")
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
            ordering = ['-created_at']
    
    def __str__(self):
            return self.title
    
    def get_tech_list(self):
            return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"   

class Achievement(models.Model):
    KIND_CHOICES = (
        ('certificate', 'Certificate'),
        ('achievement', 'Achievement'),
    )
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='certificate')
    title = models.CharField(max_length=150)
    issuer = models.CharField(max_length=150, blank=True)       # e.g. TCS iON
    date_text = models.CharField(max_length=60, blank=True)     # e.g. 12 Aug 2026
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)                          # optional certificate link
    order = models.PositiveIntegerField(default=0)              # smaller number = shown first

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title    

class Service(models.Model):
    title = models.CharField(max_length=100)
    # Small label above the title, e.g. Development
    category = models.CharField(max_length=50, blank=True)
    # Bootstrap icon class, e.g. bi-server
    icon = models.CharField(max_length=50, default='bi-laptop')
    description = models.TextField()
    # One point per line, shown under "Deliverables"
    deliverables = models.TextField(blank=True, help_text="One point per line")
    # Comma separated, shown as small technology boxes
    tech_stack = models.CharField(max_length=200, blank=True, help_text="Comma separated, e.g. Python, Django")
    # Smaller number = shown first
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

    def get_deliverable_list(self):
        # Turn the text box into a list, ignoring empty lines
        return [line.strip() for line in self.deliverables.splitlines() if line.strip()]

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]      