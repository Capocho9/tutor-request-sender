from tutors import tutor_list

def find_tutors(subject,level,availability):
  tutors = []

  for tutor in tutor_list.keys():
      if subject in tutor_list[tutor]["subjects"].keys():
          if level in tutor_list[tutor]["subjects"][subject]:
              for slot in availability:
                  if slot in tutor_list[tutor]["availability"]:
                      tutors.append(tutor)
  return tutors