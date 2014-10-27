import requests

#hack_url = 'https://hackbulgaria.com/api/students'


class TeamMatcher():
    HELLO_MESSAGE = """Hello, you can use one the following commands:
                    list_courses - this lists all the courses that are available now.
                    match_teams <course_id>, <team_size>, <group_time>
                    exit - to stop program"""

    def __init__(self):
        self.content_json = None
        self.courses_names = []
        self.courses_with_people = {}

    def get_json(self, url):
        r = requests.get(url, verify=False)
        if r.status_code == 200:
            self.content_json = r.json()
        else:
            print("Error getting Content")

    def get_courses_names(self):
        for person in self.content_json:
            for course in person['courses']:
                if course['name'] not in self.courses_names:
                    self.courses_names.append(course['name'])

    def list_courses(self):
        counter = 1
        for course in self.courses_names:
            print("[{}] {}".format(counter, course))
            counter += 1

    def get_courses_with_people(self):
        for person in self.content_json:
            for course in person['courses']:
                if course['name'] in self.courses_with_people:
                    self.courses_with_people[course['name']].append((person['name'], course['group']))
                else:
                    self.courses_with_people[course['name']] = []
                    self.courses_with_people[course['name']].append((person['name'], course['group']))

    def match_teams(self, course_id, team_size, group_time):
        working_array = []
        for person in self.courses_with_people[self.courses_names[course_id-1]]:
            if person[1] == group_time:
                working_array.append(person[0])
        return working_array

print(TeamMatcher.HELLO_MESSAGE)
a = TeamMatcher()
a.get_json('https://hackbulgaria.com/api/students')
a.get_courses_names()
a.get_courses_with_people()
while(True):
    command = input("Enter command: ")
    command = command.split(' ')
    if command[0] == 'list_courses':
        a.list_courses()
    elif command[0] == 'match_teams':
        team = a.match_teams(command[1], command[2], command[3])
        for item in team:
            print(item)
    elif command[0] == 'exit':
        print('Program exited')
        break
    else:
        print('Invalid command')
# for course in a.courses_with_people:
#     print(course, a.courses_with_people[course])
