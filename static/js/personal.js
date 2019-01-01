var user = '{{user.username}}'
const sidebar = document.querySelector('#sidebar')
const content = document.querySelector('#content')
const btnSideToggler = document.querySelector('button#sidebarCollapse')

let sidebarToggle
let sidebarToggleState
if (localStorage.getItem('sidebarToggleState') === null) {
        sidebarToggle = false
        sidebarToggleState = {'toggle': false}
        localStorage.setItem('sidebarToggleState', JSON.stringify(sidebarToggleState))
    }
    else {
       sidebarToggleState  = JSON.parse(localStorage.getItem('sidebarToggleState'))
       sidebarToggle = sidebarToggleState.toggle

    }



loadEventListeners()

if (sidebarToggle) {
	sidebar.classList.toggle('active') 
	content.classList.toggle('active')
}
else {
}

function loadEventListeners() {
   btnSideToggler.addEventListener('click', sidebarToggleEvent)
}

function sidebarToggleEvent(e) {
	if (sidebarToggle) {
		sidebarToggle = false
		sidebarToggleState.toggle = false
		localStorage.setItem('sidebarToggleState', JSON.stringify(sidebarToggleState))
	}
	else {
		sidebarToggle = true
		sidebarToggleState.toggle = true
		localStorage.setItem('sidebarToggleState', JSON.stringify(sidebarToggleState))
	}
}