import random
from context import *


##############################################################

_a = 0.20
_b = 0.20
_d = 0.20
_t = 0.20
_y = 0.20

__cost_cache = {}
def vectorCost(vector: list[list[int]], cache=True) -> float:
    key = str(vector)
    if key in __cost_cache and cache:
        return __cost_cache[key]

    overwork_penalty = 0
    skill_penalty = 0
    difficulty_penalty = 0
    deadline_penalty = 0
    assignment_violation = 0


    # unique assignment
    for assignments in vector:
        assignment_violation += abs(sum(assignments) - 1)

    staff_projects = {s.id: [] for s in STAFF_LIST}

    for projectId, assignments in enumerate(vector):
        for staffId, assigned in enumerate(assignments):
            if assigned == 1:
                staff_projects[staffId + 1] += [PROJECTS_LIST[projectId]]

    for staffId, projects in staff_projects.items():
        staff = STAFF_LIST[staffId-1]

        # capacity constraint
        total_time = sum([p.estimated_time for p in projects])
        overwork_penalty += max(0, total_time - staff.available_hours)

        for project in projects:
            # skill level constraint
            difficulty_penalty += max(0, project.difficulty - staff.skill_level)

            # skill matching
            if project.required_skill not in staff.skills:
                skill_penalty += 1

        # deadline consideration (difficulty)
        time_sum = 0
        for project in sorted(projects, key=lambda p: p.estimated_time):
            time_sum += project.estimated_time
            deadline_penalty += max(0, time_sum - project.deadline)

    out = _a * overwork_penalty + _b * skill_penalty + _d * difficulty_penalty + _t * deadline_penalty + _y * assignment_violation

    if cache:
        __cost_cache[key] = out

    return out


##############################################################


def printVector(vector: list[list[int]], cost=True) -> None:
    for projectId, assignments in enumerate(vector):
        staffList = []

        for staffId, assigned in enumerate(assignments):
            if assigned:
                staffList += [staffId + 1]

        print(f'P{projectId + 1} ->', ', '.join([f'S{staffId}' for staffId in staffList]))

    if cost:
        print(f'  Cost: {vectorCost(vector)}')


##############################################################


def randomVector(smart=False) -> list[list[int]]:
    """smart flag denotes whether it should start with single staff project assignments"""
    out = []
    
    for _ in range(len(PROJECTS_LIST)):
        if smart:
            row = [0] * len(STAFF_LIST)
            row[random.randint(0, len(STAFF_LIST) - 1)] = 1

        else:
            row = [random.randint(0, 1) for _ in range(len(STAFF_LIST))]
        
        out += [row]

    return out


##############################################################


def cloneVector(vector: list[list[int]]) -> list[list[int]]:
    return [row[:] for row in vector]


##############################################################


if __name__ == "__main__":
    vectors = {
        'perfect': [
            [1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,1,0,0,0], [0,0,0,0,1],
            [0,0,0,1,0], [1,0,0,0,0], [0,0,0,1,0], [0,0,1,0,0], [0,0,0,0,1]
        ],
        'good': [
            [1,0,0,0,0], [0,1,0,0,0], [1,0,0,0,0], [0,0,0,0,1], [0,0,1,0,0],
            [0,1,0,0,0], [0,0,0,1,0], [0,0,0,1,0], [1,0,0,0,0], [0,0,0,1,0]
        ],
        'okay': [
            [0,0,1,0,0], [0,0,1,1,0], [1,0,0,0,0], [0,0,1,0,0], [1,0,0,0,0],
            [0,0,1,0,0], [1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [1,0,0,0,0]
        ],
        'under assigned': [
            [1,0,0,0,0], [0,1,0,0,0], [0,0,0,0,0], [0,1,0,0,0], [0,0,0,0,1],
            [0,0,0,1,0], [1,0,0,0,0], [0,0,0,1,0], [0,0,1,0,0], [0,0,0,0,1]
        ],
        'over assigned': [
            [1,1,1,1,1], [0,1,0,0,0], [0,0,1,0,0], [0,1,0,0,0], [0,0,0,0,1],
            [0,0,0,1,0], [1,0,0,0,0], [0,0,0,1,0], [0,0,1,0,0], [0,0,0,0,1]
        ],
    }

    for name, vector in vectors.items():
        score = round(vectorCost(vector), 2)
        print(f'{name}: {score}')

    print()
    print("Random vector (smart=False):")
    printVector(randomVector())