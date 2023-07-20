from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from resumes.models import Resume
from resumes.serializers import ResumeSerializer


class ResumeTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            username='test_user',
            password='pQZV+3d2WfEHhE2',
        )
        self.user_2 = User.objects.create(
            username='test_user2',
            password='pQZV+3d2WfEHhE2',
        )

        self.resume1 = Resume.objects.create(
            experience='5 лет',
            portfolio='https://github.com/192117/',
            title='Python Developer',
            phone='+79939359593',
            email='test@example.com',
            owner=self.user,
        )
        self.resume2 = Resume.objects.create(
            experience='1 год',
            portfolio='https://github.com/192117/',
            title='JS Developer',
            phone='+79939359592',
            email='test@test.com',
            owner=self.user_2,
        )

    def tearDown(self):
        del self.user
        del self.user_2
        del self.resume1
        del self.resume2

    def test_get_resumes_not_auth(self):
        response = self.client.get('/resume/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Учетные данные не были предоставлены.'})

    def test_update_resume_no_auth(self):
        resume_id = Resume.objects.order_by('id').values_list('id', flat=True)[0]

        response = self.client.patch(f'/resume/{resume_id}/', data={'status': 'active'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Учетные данные не были предоставлены.'})

    def test_get_resumes_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/resume/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Resume.objects.all()))

    def test_get_user_resume_auth(self):
        self.client.force_authenticate(user=self.user)

        resumes = Resume.objects.all().order_by('id')

        response = self.client.get(f'/resume/{resumes[0].id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], Resume.objects.get(id=7).status)
        self.assertEqual(response.data['title'], Resume.objects.get(id=7).title)

    def test_get_user_resume_other_auth(self):
        self.client.force_authenticate(user=self.user_2)

        resumes = Resume.objects.all().order_by('id')

        response = self.client.get(f'/resume/{resumes[0].id}/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'У вас недостаточно прав для выполнения данного действия.'})

    def test_update_user_resume(self):
        self.client.force_authenticate(user=self.user)

        resumes = Resume.objects.all().order_by('id')

        response = self.client.patch(f'/resume/{resumes[0].id}/', data={'phone': '+79999999898'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        resume = Resume.objects.all().order_by('id')[0]
        serializer = ResumeSerializer(resume).data
        self.assertEqual(response.data, serializer)

    def test_put_not_allowed(self):
        self.client.force_authenticate(user=self.user_2)

        resumes = Resume.objects.all().order_by('id')

        response = self.client.put(f'/resume/{resumes[0].id}/', data={'phone': '+79999999898'})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_not_allowed(self):
        self.client.force_authenticate(user=self.user_2)

        resumes = Resume.objects.all().order_by('id')

        response = self.client.delete(f'/resume/{resumes[0].id}/')

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_resume_not_owner(self):
        self.client.force_authenticate(user=self.user_2)

        resumes = Resume.objects.all().order_by('id')

        resume_from = ResumeSerializer(resumes[0]).data

        response = self.client.patch(f'/resume/{resumes[0].id}/', data={'phone': '+79999999898'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'У вас недостаточно прав для выполнения данного действия.'})

        resume_to = Resume.objects.all().order_by('id')[0]
        serializer = ResumeSerializer(resume_to).data
        self.assertEqual(resume_from, serializer)
