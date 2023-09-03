import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime, timedelta

# Create dummy data
data = {
    'Candidate ID': range(1, 101),
    'Gender': ['Male', 'Female'] * 50,
    'Center': ['Center A', 'Center B', 'Center C', 'Center D'] * 25,
    'Enrollment Date': [datetime.now() - timedelta(days=i) for i in range(1, 101)],
    'Course': ['Course A', 'Course B', 'Course C', 'Course D', 'Course E'] * 20
}

df = pd.DataFrame(data)

# Create the Dash app
app = dash.Dash(__name__)

# Calculate total male and female distribution
male_count = df[df['Gender'] == 'Male']['Gender'].count()
female_count = df[df['Gender'] == 'Female']['Gender'].count()

# Calculate centerwise count of candidates
center_counts = df['Center'].value_counts()

# Calculate count of candidates enrolled in the last 30 days
recent_enrollments = df[df['Enrollment Date'] >= datetime.now() - timedelta(days=30)]['Enrollment Date'].count()

# Calculate coursewise count of candidates using gender distribution
course_counts = df.groupby(['Course', 'Gender']).size().unstack().fillna(0)

# Create the layout for the dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children=[
        html.H2(children='Gender Distribution'),
        html.Table(children=[
            html.Tr(children=[
                html.Th('Gender'),
                html.Th('Count')
            ]),
            html.Tr(children=[
                html.Td('Male'),
                html.Td(male_count)
            ]),
            html.Tr(children=[
                html.Td('Female'),
                html.Td(female_count)
            ])
        ])
    ]),

    html.Div(children=[
        html.H2(children='Centerwise Count'),
        html.Table(children=[
            html.Tr(children=[
                html.Th('Center'),
                html.Th('Count')
            ]),
            *[html.Tr(children=[
                html.Td(center),
                html.Td(count)
            ]) for center, count in center_counts.items()]
        ])
    ]),

    html.Div(children=[
        html.H2(children='Count of Candidates Enrolled in Last 30 Days'),
        html.P(f'Total: {recent_enrollments}')
    ]),

    html.Div(children=[
        html.H2(children='Coursewise Count of Candidates'),
        html.Table(children=[
            html.Tr(children=[
                html.Th('Course'),
                html.Th('Male'),
                html.Th('Female')
            ]),
            *[html.Tr(children=[
                html.Td(course),
                html.Td(course_counts.loc[course, 'Male']),
                html.Td(course_counts.loc[course, 'Female'])
            ]) for course in course_counts.index]
        ])
    ])
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

