
# My-Fitness-Log

A workout planner and log that I would want to use.

## Project Overview

A workout planner built with [django](https://www.djangoproject.com) that generates custom data tables to fit the users needs and saves them into a database for future reference. 

## Functionality

-[] display motivational quote of the day
-[] create user
    -[] log in
-[] select muscle group
    -[] choose exercises
    -[] generate random workout
    -[] provide image of individual workout
    -[] log date and time
        -[] add set
        -[] add reps
            -[] log weight being lifted
            -[] log user weight
            -[] complete workout

## Data Models

- user_name (CharField)
  - (use a custom class to generate user info)
- muscle_group (ForeignKey)
- exercise_id (CharField)
- image (CharField)
- date_time (DateTimeField)
- set (IntegerField)
- reps (IntegerField)
- user_weight (IntegerField)
- weight_lefted (IntegerField)

## Scedule

- Week 1
  - create django project
  - user log in
- Week 2
  - create muscle groups (types)
    - chest, back, legs, arms, shoulders
      - workouts associated with muscle groups
- Week 3
- styling, motivational quote

