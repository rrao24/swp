'''
Created on Mar 18, 2014

@author: encarnae
'''
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
import logging

def validate_future_date(value):
    if value > date.today():
        raise ValidationError(u'Date cannot be in the future')

def validate_past_date(value):
    if value < date.today():
        raise ValidationError(u'Date cannot be in the past')



class Post(models.Model):
    #related_name is required for all abstract classes with ForeignKey fields. See Django docs for more info
    author = models.ForeignKey(User, editable=False, blank=True, null= True, related_name="%(app_label)s_%(class)s_user")
    url_slug = models.CharField(max_length=200, editable=False)
    post_type = models.CharField(max_length=20,editable=False)
    date_posted = models.DateTimeField(auto_now_add=True) #automatically set upon object creation
    times_reported = models.IntegerField(default=0, editable=False)
    deleted = models.BooleanField(default=False, editable=False)

    def __unicode__(self):
        return self.url

    def save(self, **kwargs):
        super(Post, self).save()
        self.post_type = self.__class__.__name__.lower()
        self.url_slug = '/post/%s/%i/' % (self.post_type, self.id)
        super(Post, self).save()

    class Meta:
        abstract = True
        app_label = 'Portal'
        
class Location(models.Model):
    city = models.CharField(max_length=40)

    COUNTRIES = (
        ('AF', 'Afghanistan'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antarctica'),
        ('AG', 'Antigua and Barbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'),
        ('BS', 'Bahamas'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BB', 'Barbados'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BZ', 'Belize'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BO', 'Bolivia, Plurinational State of'),
        ('BQ', 'Bonaire, Sint Eustatius and Saba'),
        ('BA', 'Bosnia and Herzegovina'),
        ('BW', 'Botswana'),
        ('BV', 'Bouvet Island'),
        ('BR', 'Brazil'),
        ('IO', 'British Indian Ocean Territory'),
        ('BN', 'Brunei Darussalam'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Cambodia'),
        ('CM', 'Cameroon'),
        ('CA', 'Canada'),
        ('CV', 'Cape Verde'),
        ('KY', 'Cayman Islands'),
        ('CF', 'Central African Republic'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CX', 'Christmas Island'),
        ('CC', 'Cocos (Keeling) Islands'),
        ('CO', 'Colombia'),
        ('KM', 'Comoros'),
        ('CG', 'Congo'),
        ('CD', 'Congo, The Democratic Republic of the'),
        ('CK', 'Cook Islands'),
        ('CR', 'Costa Rica'),
        ('CI', "Ivory Coast"),
        ('HR', 'Croatia'),
        ('CU', 'Cuba'),
        ('CW', 'Curacao'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DK', 'Denmark'),
        ('DJ', 'Djibouti'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('EC', 'Ecuador'),
        ('EG', 'Egypt'),
        ('SV', 'El Salvador'),
        ('GQ', 'Equatorial Guinea'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('ET', 'Ethiopia'),
        ('FK', 'Falkland Islands (Malvinas)'),
        ('FO', 'Faroe Islands'),
        ('FJ', 'Fiji'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('GF', 'French Guiana'),
        ('PF', 'French Polynesia'),
        ('TF', 'French Southern Territories'),
        ('GA', 'Gabon'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('DE', 'Germany'),
        ('GH', 'Ghana'),
        ('GI', 'Gibraltar'),
        ('GR', 'Greece'),
        ('GL', 'Greenland'),
        ('GD', 'Grenada'),
        ('GP', 'Guadeloupe'),
        ('GU', 'Guam'),
        ('GT', 'Guatemala'),
        ('GG', 'Guernsey'),
        ('GN', 'Guinea'),
        ('GW', 'Guinea-bissau'),
        ('GY', 'Guyana'),
        ('HT', 'Haiti'),
        ('HM', 'Heard Island and McDonald Islands'),
        ('VA', 'Holy See (Vatican City State)'),
        ('HN', 'Honduras'),
        ('HK', 'Hong Kong'),
        ('HU', 'Hungary'),
        ('IS', 'Iceland'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran, Islamic Republic of'),
        ('IQ', 'Iraq'),
        ('IE', 'Ireland'),
        ('IM', 'Isle of Man'),
        ('IL', 'Israel'),
        ('IT', 'Italy'),
        ('JM', 'Jamaica'),
        ('JP', 'Japan'),
        ('JE', 'Jersey'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'),
        ('KE', 'Kenya'),
        ('KI', 'Kiribati'),
        ('KP', "Korea, Democratic People's Republic of"),
        ('KR', 'Korea, Republic of'),
        ('KW', 'Kuwait'),
        ('KG', 'Kyrgyzstan'),
        ('LA', "Lao People's Democratic Republic"),
        ('LV', 'Latvia'),
        ('LB', 'Lebanon'),
        ('LS', 'Lesotho'),
        ('LR', 'Liberia'),
        ('LY', 'Libya'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MO', 'Macao'),
        ('MK', 'Macedonia, The Former Yugoslav Republic of'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('MY', 'Malaysia'),
        ('MV', 'Maldives'),
        ('ML', 'Mali'),
        ('MT', 'Malta'),
        ('MH', 'Marshall Islands'),
        ('MQ', 'Martinique'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauritius'),
        ('YT', 'Mayotte'),
        ('MX', 'Mexico'),
        ('FM', 'Micronesia, Federated States of'),
        ('MD', 'Moldova, Republic of'),
        ('MC', 'Monaco'),
        ('MN', 'Mongolia'),
        ('ME', 'Montenegro'),
        ('MS', 'Montserrat'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('MM', 'Myanmar'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NL', 'Netherlands'),
        ('NC', 'New Caledonia'),
        ('NZ', 'New Zealand'),
        ('NI', 'Nicaragua'),
        ('NE', 'Niger'),
        ('NG', 'Nigeria'),
        ('NU', 'Niue'),
        ('NF', 'Norfolk Island'),
        ('MP', 'Northern Mariana Islands'),
        ('NO', 'Norway'),
        ('OM', 'Oman'),
        ('PK', 'Pakistan'),
        ('PW', 'Palau'),
        ('PS', 'Palestinian Territory, Occupied'),
        ('PA', 'Panama'),
        ('PG', 'Papua New Guinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Peru'),
        ('PH', 'Philippines'),
        ('PN', 'Pitcairn'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('PR', 'Puerto Rico'),
        ('QA', 'Qatar'),
        ('RO', 'Romania'),
        ('RU', 'Russian Federation'),
        ('RW', 'Rwanda'),
        ('SH', 'Saint Helena, Ascension and Tristan Da Cunha'),
        ('KN', 'Saint Kitts and Nevis'),
        ('LC', 'Saint Lucia'),
        ('MF', 'Saint Martin (French Part)'),
        ('PM', 'Saint Pierre and Miquelon'),
        ('VC', 'Saint Vincent and the Grenadines'),
        ('WS', 'Samoa'),
        ('SM', 'San Marino'),
        ('ST', 'Sao Tome and Principe'),
        ('SA', 'Saudi Arabia'),
        ('SN', 'Senegal'),
        ('RS', 'Serbia'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leone'),
        ('SG', 'Singapore'),
        ('SX', 'Sint Maarten (Dutch Part)'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('SB', 'Solomon Islands'),
        ('SO', 'Somalia'),
        ('ZA', 'South Africa'),
        ('GS', 'South Georgia and the South Sandwich Islands'),
        ('SS', 'South Sudan'),
        ('ES', 'Spain'),
        ('LK', 'Sri Lanka'),
        ('SD', 'Sudan'),
        ('SR', 'Suriname'),
        ('SJ', 'Svalbard and Jan Mayen'),
        ('SZ', 'Swaziland'),
        ('SE', 'Sweden'),
        ('CH', 'Switzerland'),
        ('SY', 'Syrian Arab Republic'),
        ('TW', 'Taiwan, Province of China'),
        ('TJ', 'Tajikistan'),
        ('TZ', 'Tanzania, United Republic of'),
        ('TH', 'Thailand'),
        ('TL', 'Timor-leste'),
        ('TG', 'Togo'),
        ('TK', 'Tokelau'),
        ('TO', 'Tonga'),
        ('TT', 'Trinidad and Tobago'),
        ('TN', 'Tunisia'),
        ('TR', 'Turkey'),
        ('TM', 'Turkmenistan'),
        ('TC', 'Turks and Caicos Islands'),
        ('TV', 'Tuvalu'),
        ('UG', 'Uganda'),
        ('UA', 'Ukraine'),
        ('AE', 'United Arab Emirates'),
        ('GB', 'United Kingdom'),
        ('US', 'United States'),
        ('UM', 'United States Minor Outlying Islands'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistan'),
        ('VU', 'Vanuatu'),
        ('VE', 'Venezuela, Bolivarian Republic of'),
        ('VN', 'VietNam'),
        ('VG', 'Virgin Islands, British'),
        ('WF', 'Wallis and Futuna'),
        ('EH', 'Western Sahara'),
        ('YE', 'Yemen'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe'),
    )
    country = models.CharField(max_length=2, 
                               choices=COUNTRIES, 
                               default='US')
    # All 50 states, plus the District of Columbia.
    US_STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
        ('AS', 'American Samoa'),
        ('GU', 'Guam'),
        ('MP', 'Northern Mariana Islands'),
        ('PR', 'Puerto Rico'),
        ('VI', 'Virgin Islands'),
        ('IT', 'International'),
    )

    state = models.CharField(max_length=2,
                             choices=US_STATES,
                             blank = False, null = False)
    def __unicode__(self):
        if self.country != 'US':
            return self.get_country_display()
        else:
            return "%s, %s, %s"%(self.city.title(), self.state, self.country)
    
    class Meta:
        app_label = 'Portal'

# PROJECT MARKETPLACE MODELS
class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "technologies"
        app_label = 'Portal'

class Project(Post):
    client = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=100)
    description=models.TextField()
    start_date = models.DateField(blank=True, null=True, validators = [validate_past_date])
    end_date = models.DateField( blank=True, null=True, validators = [validate_past_date])
    location = models.ForeignKey(Location, blank=True, null=True)
    technologies = models.ManyToManyField(Technology)
    password = models.CharField(max_length=350, blank=False, null=False)
        
    def __unicode__(self):
        return self.title.title()
    class Meta:
        app_label = 'Portal'

# GETHIRED PARENT MODELS
class Company(models.Model):
    name = models.CharField(max_length=30)
    avg_salary = models.DecimalField(decimal_places=2, max_digits=10, default=0, editable=False)
    avg_interview_rating = models.DecimalField(decimal_places=1, max_digits=10, default=0, editable=False)
    num_offers = models.IntegerField(default=0, editable=False)
    num_offers_to_calculate_salary = models.IntegerField(default=0, editable=False)
    num_interviews = models.IntegerField(default=0, editable=False)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural="companies"
        app_label = 'Portal'

    def add_offer(self,offer):
        self.num_offers += 1
        if (offer.pay_type == 'YS' and offer.job_type == 'FT'):
            current_avg = self.avg_salary * self.num_offers_to_calculate_salary
            self.num_offers_to_calculate_salary += 1
            self.avg_salary = (current_avg + offer.salary) / self.num_offers_to_calculate_salary
   
    def add_interview(self, interview):
        current_rating = self.avg_interview_rating * self.num_interviews
        self.num_interviews+= 1
        self.avg_interview_rating = (current_rating + interview.interview_rating) / self.num_interviews

class GetHiredPost(Post):
    degree_choices = (
            ('MI','Minor'),
            ('BA', 'B.A'),
            ('BS', 'B.S'),
            ('MA', 'M.A'),
            ('MS', 'M.S'),
            ('MB', 'MBA'),
            ('PD', 'Ph.D'),
            ('PR', 'Professional Degree'),
            ('OT','Other'),
                      )
    applicant_degree = models.CharField(max_length=2,
                                        choices=degree_choices)
    company = models.ForeignKey(Company, related_name = "%(app_label)s_%(class)s_location",blank=True, null=True)
    location = models.ForeignKey(Location, related_name="%(app_label)s_%(class)s_location",blank=True, null=True)

    title_choices = (
        ('SE', 'Software Engineer/Developer/Programmer'),
        ('WD', 'Web Developer'),
        ('ST', 'Software Engineer in Test'),
        ('DE', 'DevOps Engineer'),
        ('BA', 'Business Analyst/Programmer Analyst'),
        ('CO', 'Consultant'),
        ('DB', 'Database Administrator'),
        ('HD', 'Help Desk Technician'),
        ('NT', 'Network Architect/Engineer'),
        ('NA', 'Network Administrator'),
        ('PM', 'Product Manager')
    )

    job_title = models.CharField(max_length=2,
                                 choices=title_choices)

    type_choices = (
            ('FT','Full Time'),
            ('PT','Part Time'),
            ('PI','Paid Internship'),
            ('UI','Unpaid Internship'),
            ('CO','Co-op'),
            ('VW','Volunteer Work'),
            ('CC','Course Credit'),
            ('CW','Contract Work'),
            ('OT','Other'),
            )
    job_type = models.CharField(max_length=2,
                                choices=type_choices)

    def __unicode__(self):
        return "%s, %s"%( self.company, self.location)

    class Meta:
        abstract = True
        app_label = 'Portal'

#JOB BOARD MODELS
class Job(GetHiredPost):
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    application_deadline = models.DateField(blank=True, null=True, validators=[validate_past_date])
    application_instructions = models.TextField()
    password = models.CharField(max_length=350, blank=False, null=False)
    

    class Meta:
        app_label = 'Portal'
# GETHIRED CHILD MODELS
class Offer(GetHiredPost):
    pay_choices = (
            ('YS','Yearly Salary'),
            ('MS','Monthly Salary'),
            ('WS','Weekly Salary'),
            ('HS','Hourly Salary'),
            ('TS', 'Total Salary'),
            ('OT','Other'),
            )
    pay_type = models.CharField(max_length=2,
                                choices=pay_choices)

    display_salary = models.BooleanField()
    salary = models.DecimalField(decimal_places=2, max_digits=8)
    signing_bonus = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    relocation_bonus = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)

    offer_choices = (
            ('AC','Accepted'),
            ('NA','Not Accepted'),
            ('NE','Negotiating'),
            ('WA','Waiting'),
            ('OT','Other'),
            )
    offer_status = models.CharField(max_length=2,
                                    choices=offer_choices)
    other_details = models.TextField(blank=True, null=True)
        
    def save(self, **kwargs):
        if not self.pk:
            self.company.add_offer(self)
            self.company.save()
        super(Offer, self).save()
    
    class Meta:
        app_label = 'Portal'

class Interview(GetHiredPost):
    type_choices = (
        ('OC', 'On campus'),
        ('OS', 'On site'),
        ('TP', 'Telephone'),
        ('VC', 'Videoconference'),
        ('OT', 'Other'),
        )

    interview_type = models.CharField(max_length=2,
                                    choices=type_choices)
    interview_process = models.TextField()
    questions_asked = models.TextField()

    source_choices = (
            ('CF','Career Fair'),
            ('AO','Applied Online'),
            ('EF','Employee Referral'),
            ('PI','Previous Internship'),
            ('RE','Recruiting Event'),
            ('OT','Other'),
            )
    interview_source = models.CharField(max_length=2,
                                    choices=source_choices)
    
    date_interviewed = models.DateField(validators=[validate_future_date])

    offer_choices = (
            ('RC','Offer Received'),
            ('NR','Offer Not Received'),
            ('WA','Waiting for Offer'),
            )
    offer_status = models.CharField(max_length=2,
                                    choices=offer_choices)
    offer_details = models.OneToOneField(Offer, null=True, blank=True)
    related_interview = models.ForeignKey("Interview", blank=True, null=True)
    #this looks dumb, but it's necessary, Django won't accept int literals in the tuple
    ONE=1
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5

    rating_choices = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE,'3'),
        (FOUR,'4'),
        (FIVE,'5'),
        )
    interview_rating = models.IntegerField(choices=rating_choices)
    
    def save(self, **kwargs):
        if not self.pk:
            self.company.add_interview(self)
            self.company.save() 
        super(Interview, self).save()

    class Meta:
        app_label = 'Portal'
