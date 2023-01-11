const d = new Date()
const months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
let month = d.getMonth()
var availableMonths = [months[month], months[month+1], months[month+2]]

console.log(availableMonths)
console.log(d.toISOString().split('T')[0])


let dateElement = document.getElementById("date")
console.log(dateElement)
let today=d.toISOString().split('T')[0]
dateElement.setAttribute("value", today)
dateElement.setAttribute("min",today)
dateElement.setAttribute("max",d.getFullYear()+"-"+d.getMonth()+3+"-"+((d.getDate()<10) ? ("0"+d.getDate()):(d.getDate())))
console.log(dateElement.getAttribute("max"))