# from graphviz import Digraph

# # Create a new ERD diagram
# erd = Digraph('ERD', filename='student_enrollment', format='png')

# # Define entities (Tables)
# erd.node('Student', 'STUDENT\n(Student_ID, Name, Email, etc.)', shape='rectangle', style='filled', fillcolor='lightblue')
# erd.node('Course', 'COURSE\n(Course_ID, Course_Name, Credits, etc.)', shape='rectangle', style='filled', fillcolor='lightgreen')
# erd.node('Enrollment', 'ENROLLMENT\n(Enrollment_ID, Student_ID, Course_ID, Date_Enrolled, etc.)', shape='rectangle', style='filled', fillcolor='lightyellow')

# # Define relationships
# erd.edge('Student', 'Enrollment', label='1:M', arrowhead='normal', dir='both')
# erd.edge('Course', 'Enrollment', label='1:M', arrowhead='normal', dir='both')

# # Render and save the ERD diagram
# erd_path = "/mnt/data/student_enrollment.png"
# erd.render(erd_path, format="png", cleanup=True)

# # Return the ERD image path for display
# erd_path
print("hello")