from django.test import TestCase
from models import Offer, Interview, Location, Company
from django.contrib.auth.models import User
import populate

def create_company(company_name):
    return Company.objects.create(name=company_name)
def create_location(city_name, state_name):
    return Location.objects.create(city=city_name, state=state_name)

def create_interview(self, company_name, city_name, state_initials,
                    the_job_title, the_job_type, interview_proc,
                    the_questions_asked, interview_source_init,
                    offer_status_init, the_offer_details, rating):
    return Interview.objects.create(author=self.user,
        company = create_company(company_name),
        location = create_location(city_name, state_initials),
        job_title = the_job_title,
        job_type = the_job_type,
        interview_process = interview_proc,
        questions_asked = the_questions_asked,
        interview_source = interview_source_init,
        offer_status = offer_status_init,
        offer_details = the_offer_details,
        interview_rating = rating
        )

class GetHiredViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                username='root')
    def test_index_view_sanity_check(self):
        create_interview(self, "Google", "Mountain View", "CA",
                "SE", "FT", "Hard interviews.", "Why Google?",
                "CF", "RC", None, 1)
        response = self.client.get("/gethired/")
        self.assertEqual(response.status_code, 200, msg="Response not 200")
    def test_index_view_context(self):
        interview1 = create_interview(self, "Google", "Mountain View", "CA",
                "SE", "FT", "Hard interviews.", "Why Google?",
                "CF", "RC", None, 4)
        interview2 = create_interview(self, "Microsoft", "Redmond", "WA",
                "SE", "PT", "The interviews were not fun", "How will you save Windows Mobile?",
                "CF", "RC", None, 2)
        interview3 = create_interview(self, "Facebook", "Menlo Park", "CA", "SE",
                "FT", "I met Mark Zuckerberg", "How do you feel about virtual reality Farmville?",
                "CF", "RC", None, 5)
        response = self.client.get("/gethired/")
        self.assertTrue(interview1 in response.context['posts'])
        self.assertTrue(interview2 in response.context['posts'])
        self.assertTrue(interview3 in response.context['posts'])
    def test_post_view(self):
### Verify that posts are created and get their own post view
### This also verifies slugs are working properly
        interview1 = create_interview(self, "Google", "Mountain View", "CA",
                "SE", "FT", "Hard interviews.", "Why Google?",
                "CF", "RC", None, 4)
        interview2 = create_interview(self, "Microsoft", "Redmond", "WA",
                "SE", "PT", "The interviews were not fun", "How will you save Windows Mobile?",
                "CF", "RC", None, 2)
        interview3 = create_interview(self, "Facebook", "Menlo Park", "CA", "SE",
                "FT", "I met Mark Zuckerberg", "How do you feel about virtual reality Farmville?",
                "CF", "RC", None, 5)
        response = self.client.get("/gethired/post/Interview/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], interview1)

        response = self.client.get("/gethired/post/Interview/2/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], interview2)

        response = self.client.get("/gethired/post/Interview/3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'], interview3)

class GetHiredModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                username='root')
##uncomment this if you want to populate the database with tons of stuff
        #populate.populate()

    def test_company_model(self):
#sanity check just to see that the Company table is empty
        self.assertFalse(Company.objects.all())

        Company.objects.create(name="Google")
        Company.objects.create(name="Microsoft")
        Company.objects.create(name="SAS")
        Company.objects.create(name="Citrix")

        self.assertTrue(len(Company.objects.all()) == 4)
        self.assertTrue(Company.objects.get(name="Google"))
        self.assertTrue(Company.objects.get(name="Microsoft"))
        self.assertTrue(Company.objects.get(name="SAS"))
        self.assertTrue(Company.objects.get(name="Citrix"))

    def test_location_model(self):
#sanity check
        self.assertFalse(Location.objects.all())

        Location.objects.create(city="Raleigh", state="NC")
        Location.objects.create(city="Mountain View", state="CA")
        Location.objects.create(city="Redmond", state="WA")
        Location.objects.create(city="Cary", state="NC")

        self.assertTrue(len(Location.objects.all()) == 4)
        self.assertTrue(len(Location.objects.filter(state="NC")) == 2)
        self.assertTrue(Location.objects.get(city="Redmond"))
        self.assertTrue(Location.objects.get(city="Mountain View"))

    def test_interview_model(self):
        self.assertFalse(Interview.objects.all())
        interview_1 = Interview.objects.create(author=self.user,
        company = Company.objects.create(name="Google"),
        location = Location.objects.create(city='Mountain View', state='CA'),
        job_title = "SE",
        job_type = "FT",
        interview_process = "Hard interviews.",
        questions_asked = "Why Google?",
        interview_source = 'CF',
        offer_status = 'RC',
        offer_details = None,
        interview_rating = 1
        )
        self.assertTrue(Interview.objects.all())
        self.assertTrue(Interview.objects.get(company__name="Google"))
        self.assertTrue(Interview.objects.get(location__city="Mountain View"))
        self.assertTrue(Interview.objects.get(job_title="SE"))
        self.assertTrue(Interview.objects.get(job_type="FT"))
        self.assertTrue(Interview.objects.get(interview_process="Hard interviews."))
        self.assertTrue(Interview.objects.get(questions_asked="Why Google?"))
        self.assertTrue(Interview.objects.get(offer_status="RC"))
        self.assertTrue(Interview.objects.get(interview_rating=1))

#Assert that Interview table now has an entry
        self.assertTrue(Interview.objects.all())

    def test_offer_model(self):
        self.assertFalse(Offer.objects.all())
        offer_1 = Offer.objects.create(
        author=self.user,
        applicant_degree = 'BS',
        company = Company.objects.create(name="Google"),
        location = Location.objects.create(city='Mountain View', state='CA'),
        job_title = "SE",
        job_type = "FT",
        salary = 80000,
        signing_bonus = 10000,
        relocation_bonus = 10000,
        offer_status = 'RC',
        other_details = "Liked the offer, good benefits",
        display_salary = True
        )
        self.assertTrue(Offer.objects.all())
        self.assertTrue(Offer.objects.get(company__name="Google"))
        self.assertTrue(Offer.objects.get(location__city="Mountain View"))
        self.assertTrue(Offer.objects.get(applicant_degree='BS'))
        self.assertTrue(Offer.objects.get(job_title="SE"))
        self.assertTrue(Offer.objects.get(job_type="FT"))
        self.assertTrue(Offer.objects.get(salary=80000))
        self.assertTrue(Offer.objects.get(signing_bonus=10000))
        self.assertTrue(Offer.objects.get(relocation_bonus=10000))
        self.assertTrue(Offer.objects.get(offer_status='RC'))
        self.assertTrue(Offer.objects.get(other_details='Liked the offer, good benefits'))
        self.assertTrue(Offer.objects.get(display_salary=True))
class GetHiredModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                username='root')
##uncomment this if you want to populate the database with tons of stuff
        #populate.populate()

    def test_company_model(self):
#sanity check just to see that the Company table is empty
        self.assertFalse(Company.objects.all())

        Company.objects.create(name="Google")
        Company.objects.create(name="Microsoft")
        Company.objects.create(name="SAS")
        Company.objects.create(name="Citrix")

        self.assertTrue(len(Company.objects.all()) == 4)
        self.assertTrue(Company.objects.get(name="Google"))
        self.assertTrue(Company.objects.get(name="Microsoft"))
        self.assertTrue(Company.objects.get(name="SAS"))
        self.assertTrue(Company.objects.get(name="Citrix"))

    def test_location_model(self):
#sanity check
        self.assertFalse(Location.objects.all())

        Location.objects.create(city="Raleigh", state="NC")
        Location.objects.create(city="Mountain View", state="CA")
        Location.objects.create(city="Redmond", state="WA")
        Location.objects.create(city="Cary", state="NC")

        self.assertTrue(len(Location.objects.all()) == 4)
        self.assertTrue(len(Location.objects.filter(state="NC")) == 2)
        self.assertTrue(Location.objects.get(city="Redmond"))
        self.assertTrue(Location.objects.get(city="Mountain View"))

    def test_interview_model(self):
        self.assertFalse(Interview.objects.all())
        interview_1 = Interview.objects.create(author=self.user,
        company = Company.objects.create(name="Google"),
        location = Location.objects.create(city='Mountain View', state='CA'),
        job_title = "SE",
        job_type = "FT",
        interview_process = "Hard interviews.",
        questions_asked = "Why Google?",
        interview_source = 'CF',
        offer_status = 'RC',
        offer_details = None,
        interview_rating = 1
        )
        self.assertTrue(Interview.objects.all())
        self.assertTrue(Interview.objects.get(company__name="Google"))
        self.assertTrue(Interview.objects.get(location__city="Mountain View"))
        self.assertTrue(Interview.objects.get(job_title="SE"))
        self.assertTrue(Interview.objects.get(job_type="FT"))
        self.assertTrue(Interview.objects.get(interview_process="Hard interviews."))
        self.assertTrue(Interview.objects.get(questions_asked="Why Google?"))
        self.assertTrue(Interview.objects.get(offer_status="RC"))
        self.assertTrue(Interview.objects.get(interview_rating=1))

#Assert that Interview table now has an entry
        self.assertTrue(Interview.objects.all())

    def test_offer_model(self):
        self.assertFalse(Offer.objects.all())
        offer_1 = Offer.objects.create(
        author=self.user,
        applicant_degree = 'BS',
        company = Company.objects.create(name="Google"),
        location = Location.objects.create(city='Mountain View', state='CA'),
        job_title = "SE",
        job_type = "FT",
        salary = 80000,
        signing_bonus = 10000,
        relocation_bonus = 10000,
        offer_status = 'RC',
        other_details = "Liked the offer, good benefits",
        )
        self.assertTrue(Offer.objects.all())
        self.assertTrue(Offer.objects.get(company__name="Google"))
        self.assertTrue(Offer.objects.get(location__city="Mountain View"))
        self.assertTrue(Offer.objects.get(applicant_degree='BS'))
        self.assertTrue(Offer.objects.get(job_title="SE"))
        self.assertTrue(Offer.objects.get(job_type="FT"))
        self.assertTrue(Offer.objects.get(salary=80000))
        self.assertTrue(Offer.objects.get(signing_bonus=10000))
        self.assertTrue(Offer.objects.get(relocation_bonus=10000))
        self.assertTrue(Offer.objects.get(offer_status='RC'))
        self.assertTrue(Offer.objects.get(other_details='Liked the offer, good benefits'))
