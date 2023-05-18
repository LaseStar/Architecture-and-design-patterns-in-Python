from datetime import date



# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


# For test, then will delete
def method_front(request):
    request['method'] = 'GET'


# fronts = [secret_front, other_front, method_front]

# routes = {
#     '/': Index(),
#     '/about/': About(),
#     '/price/': Price(),
#     '/study_programs/': StudyPrograms(),
#     '/courses-list/': CoursesList(),
#     '/create-course/': CreateCourse(),
#     '/create-category/': CreateCategory(),
#     '/category-list/': CategoryList(),
#     '/copy-course/': CopyCourse(),

fronts = [secret_front, other_front]
