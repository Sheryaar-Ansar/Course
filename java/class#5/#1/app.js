const totalMarks = 300
const students = [
    {
        name : 'Sheryaar',
        scienceMarks : 80,
        mathMarks : 95,
        urduMarks : 98,
    },
    {
        name : 'Afnan',
        scienceMarks : 50,
        mathMarks : 65,
        urduMarks : 78,
    },
    {
        name : 'Muhammad',
        scienceMarks : 20,
        mathMarks : 35,
        urduMarks : 48,
    }
    
]

function calculateMarks(students){
    const total = students.scienceMarks + students.mathMarks + students.urduMarks;
    const percentage = (total / totalMarks)*100
    return {total, percentage}
}

for(let i = 0;i < students.length; i++){
    const result = calculateMarks(students[i])
    console.log('---------------------------')
    console.log('Name:', students[i].name)
    console.log('Science Marks:', students[i].scienceMarks)
    console.log('Maths Marks:', students[i].mathMarks)
    console.log('Urdu Marks:', students[i].urduMarks)
    console.log('Total Marks:', totalMarks)
    console.log('Obtained Marks:', result.total)
    console.log('Percentage:', result.percentage+'%')
    result.percentage >=40 ? console.log('Congrats! You`re Pass') : console.log('Better Luck Next Time, FAILED!')
}