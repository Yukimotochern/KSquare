const btnNewConcept = document.querySelector('div#concepts.board form div div button.btnNewConcept')
const inputSearchConcept = document.querySelector('div#concepts.board form div div input#btnSearchConcepts')
const listGroupConcepts = document.querySelector('div#all_concepts div.list-group.list-group-flush')
const editTitle = document.querySelector('input.inputConceptTitle')
const editSummary = document.querySelector('textarea.textareaConceptSummary')
const aConceptToCopy = document.querySelector('a.toCopy.d-none')
const scroll = document.querySelector('#all_concepts.scroll')
const btnSaveAdd = document.querySelector('#saveAddConcept')
const btnDeleteConcept = document.querySelector('#deleteConcept')
const btnSaveConcept = document.querySelector('#saveConcept')
var currentEditingConcept

var csrf_token = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
window.addEventListener('load', function(event){
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            }
        });
    })
loadEventListeners()


function loadEventListeners() {
    

    for (let tagConcept of Array.from(listGroupConcepts.children)) {
    	tagConcept.addEventListener('click', change)
    }
    currentEditingConcept = listGroupConcepts.firstElementChild
    if (currentEditingConcept) {
    	currentEditingConcept.click()
    }
    btnNewConcept.addEventListener('click', addNewConcept)
    btnSaveAdd.addEventListener('click', saveAdd)
    btnSaveConcept.addEventListener('click', saveConcept)
    btnDeleteConcept.addEventListener('click', deleteConcept)
}


function change(event) {
	let tabConcept = this
	if ('notSaved' in this.classList) {
		btnSaveAdd.textContent = '儲存後再新增'
		btnSaveConcept.textContent = '儲存概念'
	}
	else {
		btnSaveAdd.textContent = '修改後再新增'
		btnSaveConcept.textContent = '儲存修改'
	}
	currentEditingConcept.classList.remove('active')
	tabConcept.classList.add('active')
	currentEditingConcept = tabConcept
	// console.log(typeof tabConcept)
	// console.log(tabConcept)
	let title = tabConcept.querySelector('h5').textContent
	let summary = tabConcept.querySelector('p.concept-summary').textContent
	if (title != '未儲存概念') {
		editTitle.value = title
	}
	else {
		editTitle.value = ""
	}
	if (summary != '保持冷靜，寫點東西'){
		editSummary.value = summary
	}
	else {
		editSummary.value = ''
	}
	event.preventDefault()
}

function addNewConcept(event) {
	aToAdd = aConceptToCopy.cloneNode(true)
	aToAdd.classList.remove('d-none')
	aToAdd.addEventListener('click', change)
	aToAdd.querySelector('small.owner').textContent = 'by ' + user
	if (currentEditingConcept) {
		currentEditingConcept.classList.remove('active')
	}
	currentEditingConcept = aToAdd
	editTitle.value = ""
	editSummary.value = ""
	if (listGroupConcepts.firstElementChild) {
		listGroupConcepts.insertBefore(aToAdd, listGroupConcepts.firstElementChild)
	}
	else {
		listGroupConcepts.appendChild(currentEditingConcept)
	}
	scroll.scrollTop = 0
	editTitle.focus()
	if (event) {
		event.preventDefault()
	}
}

function saveAdd(e) {
	title = editTitle.value
	summary = editSummary.value
	if(currentEditingConcept.classList.contains('notSaved')) {
		$.ajax({
	         url: '',
	         method: 'POST',
	            data: {
	            action: 'newConcept',
	            title: title,
	            summary: summary,
	         },
	     }).then(
	         function success(ob){
	         	currentEditingConcept.classList.remove('notSaved')
	         	currentEditingConcept.querySelector('h5').textContent = editTitle.value
	         	currentEditingConcept.querySelector('p.concept-summary').textContent = editSummary.value
				addNewConcept()
	         },
	         function fail(status){
	         	alert('Something Went Wrong: ' + status)
	         }
	    )
	}
	else {
		id = currentEditingConcept.querySelector('input[type="hidden"]').value
		$.ajax({
	         url: '',
	         method: 'POST',
	            data: {
	            action: 'updateConcept',
	            title: title,
	            summary: summary,
	            id: id,
	         },
	     }).then(
	         function success(ob){
	         	currentEditingConcept.querySelector('h5').textContent = editTitle.value
	         	currentEditingConcept.querySelector('p.concept-summary').textContent = editSummary.value
	         	addNewConcept()
	         },
	         function fail(status){
	         	alert('Something Went Wrong: ' + status)
	         }
	    )
	}
}

function saveConcept(e) {
	title = editTitle.value
	summary = editSummary.value
	if(currentEditingConcept.classList.contains('notSaved')) {
		$.ajax({
	         url: '',
	         method: 'POST',
	            data: {
	            action: 'newConcept',
	            title: title,
	            summary: summary,
	         },
	     }).then(
	         function success(ob){
	         	currentEditingConcept.classList.remove('notSaved')
	         	currentEditingConcept.querySelector('h5').textContent = editTitle.value
	         	currentEditingConcept.querySelector('p.concept-summary').textContent = editSummary.value
	         },
	         function fail(status){
	         	alert('Something Went Wrong: ' + status)
	         }
	    )
	}
	else {
		id = currentEditingConcept.querySelector('input[type="hidden"]').value
		$.ajax({
	         url: '',
	         method: 'POST',
	            data: {
	            action: 'updateConcept',
	            title: title,
	            summary: summary,
	            id: id,
	         },
	     }).then(
	         function success(ob){
	         	currentEditingConcept.querySelector('h5').textContent = editTitle.value
	         	currentEditingConcept.querySelector('p.concept-summary').textContent = editSummary.value
	         },
	         function fail(status){
	         	alert('Something Went Wrong: ' + status)
	         }
	    )
	}
}

function deleteConcept(e) {
	if(currentEditingConcept.classList.contains('notSaved')) {
		currentEditingConcept.remove()
		nextFocus = currentEditingConcept.nextElementSibling
		if(nextFocus) {
     		currentEditingConcept = nextFocus
     		nextFocus.click()
     	}
     	else {
     		editTitle.value = ""
     		editSummary.value = ""
     	}
	}
	else {
		id = currentEditingConcept.querySelector('input[type="hidden"]').value
		$.ajax({
	         url: '',
	         method: 'POST',
	            data: {
	            action: 'deleteConcept',
	            id: id,
	         },
	     }).then(
	         function success(ob){
	         	nextFocus = currentEditingConcept.nextElementSibling
	         	currentEditingConcept.remove()
	         	if(nextFocus) {
	         		currentEditingConcept = nextFocus
	         		nextFocus.click()
	         	}
	         	else {
	         		editTitle.value = ""
	         		editSummary.value = ""
	         	}

	         },
	         function fail(status){
	         }
	    )
	}
}







