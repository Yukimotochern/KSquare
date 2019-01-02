const sidebar = document.querySelector('#sidebar')
const content = document.querySelector('#content')
const btnSideToggler = document.querySelector('button#sidebarCollapse')
const links = document.querySelectorAll('#create-tab  .nav-link')

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


function loadEventListeners() {
   btnSideToggler.addEventListener('click', sidebarToggleEvent)
}

function sidebarToggleEvent(e) {
	if (sidebarToggle) {
		sidebarToggle = false
		sidebarToggleState.toggle = false
		localStorage.setItem('sidebarToggleState', JSON.stringify(sidebarToggleState))
		tabChange(true)
	}
	else {
		sidebarToggle = true
		sidebarToggleState.toggle = true
		localStorage.setItem('sidebarToggleState', JSON.stringify(sidebarToggleState))
		tabChange(false)
	}
}

function tabChange(isOpen) {
	if (isOpen) {
		for (let link of Array.from(links)) {
			str = link.href
			if (str.endsWith('0')) {
				link.href = str.slice(0, str.length-1) + '1'
			}
		}
	}
	else {
		for (let link of Array.from(links)) {
			str = link.href
			if (str.endsWith('1')) {
				link.href = str.slice(0, str.length-1) + '0'
			}
		}

	}
}




















