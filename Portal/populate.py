import os
from random import choice, randint
from models import Offer, Interview, Location, Company, Project, Job, Technology
from django.contrib.auth.models import User
from datetime import datetime
def populateGetHired():

    #companies and locations
    Company.objects.create(name='Microsoft')
    Company.objects.create(name='Facebook')
    Company.objects.create(name='Google')
    Company.objects.create(name='Epic')
    Company.objects.create(name='IBM')
    Company.objects.create(name='Red Hat')
    Company.objects.create(name='Citrix')

    Location.objects.create(city='Denver',state='CO')
    Location.objects.create(city='Madison',state='WI')
    Location.objects.create(city='Baltimore',state='MD')
    Location.objects.create(city='San Jose',state='CA')
    Location.objects.create(city='New York',state='NY')
    Location.objects.create(city='Boston',state='MA')
    Location.objects.create(city='Raleigh',state='NC')
    Location.objects.create(city='San Francisco',state='CA')

    companies = Company.objects.all()
    locations = Location.objects.all()
    user = User.objects.get(username='root')
    degree = ['MI','BA','BS']
    title = ['SE','WD','ST','DE','BA','CO']
    job_type = ['FT','PT','PI','CO']
    
    pay_type = ['YS']
    salaries = [50000, 60000, 70000, 80000, 10000]
    bonus = [3000, 10000, 5000]
    offer_status = ['AC','NA','NE','WA']
    details = "Liked the offer, benefits are great"
	
    interview_process = "Submitted my resume through my school's career center. Contacted a couple weeks later to schedule a phone interview. Couldn't understand the interviewer. Was notified via email a few weeks later that I was not selected for the final round. "

    questions = '''What are your strengths?
What are your weaknesses?
Where do you see yourself in 5 years?
What is your salary expectation?'''
    
    interview_source = ['CF','AO','RE']
    interview_offer = ['RC','NR','WA']
    interview_type = ['OC', 'OS', 'TP', 'VC']

    #PROJECTS
    date_interviewed = datetime.now()
    for i in range(0,20):
        add_Offer(user,
                  choice(degree),
                  choice(companies),
                  choice(locations),
                  choice(title),
                  choice(job_type),
                  choice(pay_type),
                  choice(salaries),
                  choice(bonus),
                  choice(bonus),
                  choice(offer_status),
                  details)

        add_Interview(user,
                      choice(degree),
                      choice(companies),
                      choice(locations),
                      choice(title),
                      choice(job_type),
                      interview_process,
                      questions,
                      choice(interview_source),
                      choice(interview_type),
                      choice(interview_offer),
                      randint(1,5), date_interviewed)


def add_Interview(user, degree, company, location, title, type, process, questions, source, interview_type, status, rating, date_interviewed):
    p = Interview.objects.create(author= user, 
								 applicant_degree = degree, 
                                 company = company,
                                 location = location,
                                 job_title = title,
                                 job_type = type,
                                 interview_process = process,
                                 questions_asked = questions,
                                 interview_source = source,
                                 interview_type = interview_type,
                                 offer_status = status,
                                 offer_details = None,
                                 interview_rating = rating,
                                 date_interviewed = date_interviewed)
    print("Added interview for company %s"%p.company)
    print("The interview rating was %i"%(p.interview_rating))
    print("The number of interviews for company %s is now %i"%(p.company, p.company.num_interviews))
    print("The average interview rating is %.2f"%(p.company.avg_interview_rating))
    print("END")

def add_Offer(user, degree, company, location, title, type, pay_type, salary, bonus, relocation, status, details):
    o = Offer.objects.create(author= user, 
								 applicant_degree = degree, 
                                 company = company,
                                 location = location,
                                 job_title = title,
                                 job_type = type,
                                 salary = salary,
                                 display_salary = choice([True,False]),
                                 pay_type = pay_type,
                                 signing_bonus=bonus,
                                 relocation_bonus=relocation,
                                 offer_status=status,
                                 other_details=details)
def populateProject():

    #technologies
    Technology.objects.create(name='Java')
    Technology.objects.create(name='C++')
    Technology.objects.create(name='DirectX')
    Technology.objects.create(name='JavaScript')
    Technology.objects.create(name='Python')
    Technology.objects.create(name='Android')
    Technology.objects.create(name='IOS')

    technologies = Technology.objects.all()
    locations = Location.objects.all()
    user = User.objects.get(username='root')
    
    emails = ['encarnae@cs.unc.edu','foo@bar.com', 'leroy@jenkins.org']
    names = ['Eliezer Encarnacion', 'Danyal Fiza', 'Sasha Karpinski', 'Andrew Park']
    titles = ['New UNC Mobile app', 'Let\'s build a robot!', 'Anyone wanna learn IOS?', 'Need help building a personal site', 'Need programmer for a new startup']
    description = '''This is a project that could extremely benefitial
                      for your future employability. If you can learn to 
                      do the stuff we will be doing here, you will acquire a 
                      very useful set of skills that will help you get a job
                      once you graduate.'''

    #PROJECTS
    start_date = datetime.now()

    for i in range(0,20):
        add_Project(user,
                  choice(names),
                  choice(emails),
                  choice(titles),
                  description,
                  start_date,
                  choice(locations),
                  technologies)


def add_Project(user, client, email, title, description, start_date, location, technologies):
    p = Project.objects.create(author= user,
                                client = client,
                                email = email,
                                title = title,
                                description = description,
                                start_date = start_date,
                                location = location, password="123")
    p.technologies.add(choice(technologies))
    p.technologies.add(choice(technologies))

def populateJobs():
    companies = Company.objects.all()
    locations = Location.objects.all()
    technologies = Technology.objects.all()

    user = User.objects.get(username='root')
    degree = ['MI','BA','BS']
    title = ['SE','WD','ST','DE','BA','CO']
    job_type = ['FT','PT','PI','CO']
    deadline = datetime(2014,5,15)

    description = """Responsibilities:
                  Determines operational feasibility by evaluating analysis, problem definition, requirements, solution development, and proposed solutions.
                  Documents and demonstrates solutions by developing documentation, flowcharts, layouts, diagrams, charts, code comments and clear code.
                  Prepares and installs solutions by determining and designing system specifications, standards, and programming.
                  Improves operations by conducting systems analysis; recommending changes in policies and procedures.
                  Obtains and licenses software by obtaining required information from vendors; recommending purchases; testing and approving products.
                  Updates job knowledge by studying state-of-the-art development tools, programming techniques, and computing equipment;
                  Protects operations by keeping information confidential.
                  Provides information by collecting, analyzing, and summarizing development and service issues.
                  Accomplishes engineering and organization mission by completing related results as needed.
                  Develops software solutions by studying information needs; conferring with users; 
                  """
    instructions = "Send me your resume at john@example.com"
    for i in range(20):
      add_job(user, choice(degree), choice(companies), choice(locations),choice(title), choice(job_type), description, instructions, deadline, technologies)

def add_job(user, degree, company, location, title, type, description, instructions,deadline, technologies):
    p = Job.objects.create(author= user, 
                 applicant_degree = degree, 
                                 company = company,
                                 location = location,
                                 job_title = title,
                                 job_type = type,
                                 description = description,
                                 application_instructions = instructions,
                                 application_deadline = deadline,
                                 )

    p.technologies.add(choice(technologies))
    p.technologies.add(choice(technologies))

def populate():
    populateGetHired()
    populateProject()
    populateJobs()


# Start execution here!
if __name__ == '__main__':
    print "Starting population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CSPortal.settings") 
