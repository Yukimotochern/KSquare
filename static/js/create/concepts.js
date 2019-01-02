const btnNewConcept = document.querySelector('div#concepts.board form div div button.btnNewConcept')
const inputSearchConcept = document.querySelector('div#concepts.board form div div input#inputSearchConcepts')
const listGroupConcepts = document.querySelector('div#all_concepts div.list-group.list-group-flush')
const editTitle = document.querySelector('input.inputConceptTitle')
const editSummary = document.querySelector('textarea.textareaConceptSummary')
const aConceptToCopy = document.querySelector('a.toCopy.d-none')
const scroll = document.querySelector('#all_concepts.scroll')
const btnSaveAdd = document.querySelector('#saveAddConcept')
const btnDeleteConcept = document.querySelector('#deleteConcept')
const btnSaveConcept = document.querySelector('#saveConcept')
const aNoConceptToCopy = document.querySelector('#noConcept')
const aNoResultToCopy = document.querySelector('#noResult')
var noConceptInlist = document.querySelector('.noConcept.inList')
var noResultInlist = document.querySelector('.noResult.inList')
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
    	if (tagConcept.classList.contains('noConcept')){
    		tagConcept.addEventListener('click', addNewConcept)
    	}
    	else {
    		tagConcept.addEventListener('click', change)
    	}
    	if (tagConcept.classList.contains('active')) {
    		currentEditingConcept = tagConcept
    	}
    }
    btnNewConcept.addEventListener('click', addNewConcept)
    btnSaveAdd.addEventListener('click', saveAdd)
    btnSaveConcept.addEventListener('click', saveConcept)
    btnDeleteConcept.addEventListener('click', deleteConcept)
    inputSearchConcept.addEventListener('input', searchConcepts)
    inputSearchConcept.addEventListener('keypress', searchConcepts)
}


function change(event) {

	let tabConcept = this

	// Update Editor
	updateEditor(this.classList.contains('notSaved'), getTitleInGroup(this)==="", tabConcept)

	// Jump in Group
	if (currentEditingConcept) {
		currentEditingConcept.classList.remove('active')
	}
	tabConcept.classList.add('active')
	currentEditingConcept = tabConcept

	if (event){
		event.preventDefault()
	}
}

function addNewConcept(event) {
	let aToAdd = addNewConceptInGroup()
	updateEditor(true, true, aToAdd)
	editTitle.focus()
	if (event) {
		event.preventDefault()
	}
}

function addNewConceptInGroup() {
	if (noConceptInlist) {
		noConceptInlist.remove()
		noConceptInlist = null
	}
	if (noResultInlist) {
		noResultInlist.remove()
		noResultInlist = null
	}
	let aToAdd = aConceptToCopy.cloneNode(true)
	aToAdd.classList.remove('d-none')
	aToAdd.addEventListener('click', change)
	if (user) {
		aToAdd.querySelector('small.owner').textContent = 'by ' + user
	}
	else {
		aToAdd.querySelector('small.owner').textContent = 'by Somebody'
	}
	
	if (currentEditingConcept) {
		currentEditingConcept.classList.remove('active')
	}
	currentEditingConcept = aToAdd
	currentEditingConcept.classList.add('active')

	if (listGroupConcepts.firstElementChild) {
		listGroupConcepts.insertBefore(aToAdd, listGroupConcepts.firstElementChild)
	}
	else {
		listGroupConcepts.appendChild(aToAdd)
	}
	scroll.scrollTop = 0
	return aToAdd
}

function saveAdd(e) {
	title = editTitle.value
	summary = editSummary.value
	conceptRequest(title, summary, currentEditingConcept, 'saveAdd')
}

function saveConcept(e) {
	title = editTitle.value
	summary = editSummary.value
	conceptRequest(title, summary, currentEditingConcept, 'saveConcept')
}

function deleteConcept(e) {
	if (currentEditingConcept) {
		id = currentEditingConcept.querySelector('input[type="hidden"]').value
	}
	else {
		id = ""
	}
	deleteConceptRequest(id)
}

function searchConcepts(event) {
	searchTextArray = event.target.value.toLowerCase().trim().split(' ')
	if (noConceptInlist) {
		return
	}
	let hasResult = false
	let clicked = false
	children = listGroupConcepts.children
	for (let i = 0; i < children.length; i++) {
		if (children[i].classList.contains('inList')) {
			continue
		}
		let found = false
		title = getTitleInGroup(children[i]).toLowerCase()
		summary = getSummaryInGroup(children[i]).toLowerCase()
		for (let j = 0; j < searchTextArray.length; j++) {
			if (title.includes(searchTextArray[j]) || summary.includes(searchTextArray[j])) {
				found = true
				hasResult = true
				if (!clicked) {
					children[i].click()
					clicked = true
				}
			}
		}
		if (found) {
			children[i].classList.remove('d-none')
		}
		else {
			children[i].classList.add('d-none')
		}
	}
	if (hasResult && noResultInlist) {
		noResultInlist.remove()
		noResultInlist = null
	} 
	else if (!hasResult && !noResultInlist) {
		console.log(1)
		aNoResultToAdd = aNoResultToCopy.cloneNode(true)
		aNoResultToAdd.classList.add('inList')
		aNoResultToAdd.classList.remove('d-none')
		aNoResultToAdd.removeAttribute('id')
		noResultInlist = aNoResultToAdd
		listGroupConcepts.insertBefore(aNoResultToAdd, listGroupConcepts.firstElementChild)
	}
	else {

	}
	if (event.code ==='Enter') {
		event.preventDefault()
	}
}

function getTitleInGroup(a) {
	return a.querySelector('h5').textContent
}

function getSummaryInGroup(a) {
	return a.querySelector('p.concept-summary').textContent
}

function getIdInGroup(a) {
	return a.querySelector('input[type="hidden"]').value
}

function setInGroup(currentTab, title, summary, id) {
	if (currentTab) {
		if (title!="") {
			currentTab.querySelector('h5').textContent = title
		}
		else {
			currentTab.querySelector('h5').textContent = '未命名概念'
		}
		if (summary != "") {
			currentTab.querySelector('p.concept-summary').textContent = summary
		}
		else {
			currentTab.querySelector('p.concept-summary').textContent = '保持冷靜，寫點東西'
		}
		currentTab.querySelector('input[type="hidden"]').value = id
	}
	else {

	}
}

function updateCurrentEditingConcept(title, summary, id, action) {
	if (action==='delete') {
		next = getNextFocus()
		if (currentEditingConcept) {
			currentEditingConcept.remove()
		}
		if (next) {
			currentEditingConcept = next
			currentEditingConcept.click()
		}
		else {
			currentEditingConcept = undefined
			setNoConcept()
		}
	}
	else {
		if (!currentEditingConcept){
			addNewConceptInGroup()
		}
		setInGroup(currentEditingConcept, title, summary, id)
	}
}

function getNextFocus() {
	if (currentEditingConcept) {
		nextFocus = currentEditingConcept.nextElementSibling
		if (nextFocus) {
			return nextFocus
		}
		else {
			return currentEditingConcept.previousElementSibling
		}
	}
	else {
		return listGroupConcepts.firstElementChild
	}
}

function setNoConcept() {
	let aNoToAdd = aNoConceptToCopy.cloneNode(true)
	aNoToAdd.classList.remove('d-none')
	aNoToAdd.removeAttribute('id')
	aNoToAdd.classList.add('inList')
	aNoToAdd.addEventListener('click', addNewConcept)
	noConceptInlist = aNoToAdd
	listGroupConcepts.appendChild(aNoToAdd)
}

function updateEditor(notSaved, isEmpty, currentTab) {
	if (isEmpty) {
		editTitle.value = ""
		
	}
	else {
		tabTitle = getTitleInGroup(currentTab)
		if (tabTitle==="未命名概念" || tabTitle==="未儲存概念") {
			editTitle.value = ""
		}
		else {
			editTitle.value = tabTitle
		}
	}
	summary = getSummaryInGroup(currentTab)
	if (summary==="保持冷靜，寫點東西") {
		editSummary.value = ""
	}
	else {
		editSummary.value =  getSummaryInGroup(currentTab)
	}
	btnSaveConcept.classList.remove('d-none')
	btnSaveAdd.classList.remove('d-none') 
	btnDeleteConcept.classList.remove('d-none') 
	if (notSaved) {
		btnSaveConcept.textContent = '儲存概念'
		btnSaveAdd.textContent = '儲存後再新增'
		btnDeleteConcept.textContent = '取消新增'
	}
	else {
		btnSaveConcept.textContent = '儲存修改'
		btnSaveAdd.textContent = '修改後再新增'
		btnDeleteConcept.textContent = '刪除概念'
	}

}

function clearEditor() {
	editTitle.value = ""
	editSummary.value =  ""
	btnSaveAdd.classList.add('d-none') 
	btnDeleteConcept.classList.add('d-none') 
	btnSaveConcept.textContent = '新增概念'
}

function conceptRequest(title, summary, currentTab, from) {
	if (currentEditingConcept) {
		if (currentEditingConcept.classList.contains('notSaved')) {
			action = 'newConcept'
		}
		else {
			action = 'updateConcept'
		}
	}
	else {
		action = "newConcept"
	}
	$.ajax({
	        url: '',
	        method: 'POST',
            data: {
            	action: action,
            	title: title,
            	summary: summary,
	        	},
	     }).then(
	         function success(ob){
	     		updateCurrentEditingConcept(title, summary, ob.id, 'addOrUpdate')
	     		updateEditor(false, title==="", currentTab)
	     		currentEditingConcept.classList.remove('notSaved')
	         	if (from=="saveAdd") {
	         		addNewConcept()
	         	}
	         },
	         function fail(status){
	         	alert('Something Went Wrong: ' + status)
	         	
	         }
	    )
}

function deleteConceptRequest(id) {
	if (id==="") {
		updateCurrentEditingConcept("", "", "", 'delete')
		if (!currentEditingConcept) {
			clearEditor()
		}
	}
	else {
		$.ajax({
	         url: '',
	         method: 'POST',
	            data: {
	            action: 'deleteConcept',
	            id: id,
	         },
	     }).then(
	         function success(ob){
         		updateCurrentEditingConcept("", "", "", 'delete')
         		if (!currentEditingConcept) {
					clearEditor()
				}
	         },
	         function fail(status){
	         	alert('Something Went Wrong: ' + status)
	         }
	    )
	}
}



















