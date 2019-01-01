const btnNewConcept = document.querySelector('#all_concepts.card a.card-footer.btn')
const formAddConceptCopy = document.querySelector('#formAddConcept.card-footer')
const cardConcepts = document.querySelector('#all_concepts')
const cardBodyConcepts = document.querySelector('#all_concepts .card-body')
const btnAddConcept = document.querySelector('#all_concepts.card .card-footer > button.btn.btn-success')
const btnCancelAddConcept = document.querySelector('#all_concepts.card #formAddConcept.card-footer div button#addConceptCancel')
const listGroupConcepts = document.querySelector('#all_concepts.card .card-body .list-group')

var csrf_token = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

loadEventListeners()


function loadEventListeners() {
    window.addEventListener('load', function(event){
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            }
        });
    })
    btnNewConcept.addEventListener('click', showAddConcept)
}

function showAddConcept(e){
    e.preventDefault()
    btnNewConcept.classList.add('d-none')
    formToAdd = formAddConceptCopy.cloneNode(true)
    formToAdd.classList.remove('d-none')
    formToAdd.querySelector('.btn.btn-success').addEventListener('click', newConcept)
    formToAdd.querySelector('button#addConceptCancel').addEventListener('click', cancelAddConcept)
    // cardBodyConcepts.scrollTop = cardBodyConcepts.scrollHeight
    cardConcepts.appendChild(formToAdd)
    formToAdd.querySelector('textarea').focus()
    cardBodyConcepts.scrollTop = cardBodyConcepts.scrollHeight

}

function cancelAddConcept(e){
    const formToRemove = document.querySelector('#all_concepts.card #formAddConcept.card-footer')
    formToRemove.remove()
    btnNewConcept.classList.remove('d-none')
}

function newConcept(e){
     let title = document.getElementById('newConceptTitle').value
     $.ajax({
         url: '',
         method: 'POST',
            data: {
            action: 'newConcept',
            title: title,
         },
     }).then(
         function success(ob){
            const preConceptToCopy = document.querySelector('.board a.list-group-item.d-none')
            const conceptToCopy = preConceptToCopy.cloneNode(true)
            conceptToCopy.classList.remove('d-none')
            conceptToCopy.querySelector('input').value = ob.id
            console.log(ob.id)
            console.log(title)
            conceptToCopy.querySelector('h5').textContent = title
            conceptToCopy.querySelector('small.create_time').textContent = 'just now'
            conceptToCopy.querySelector('small.created_by ').textContent = 'created by ' + ob.owner
            listGroupConcepts.appendChild(conceptToCopy)
            cardBodyConcepts.scrollTop = cardBodyConcepts.scrollHeight
            continueTextarea = document.querySelector('#all_concepts #formAddConcept div textarea')
            continueTextarea.value = ""
            continueTextarea.focus()
         },
         function fail(status){
            alert('Something Went Wrong' + status)
            cancelAddConcept()
         }
     )
}

function doNothing(e){

}

function clearAndResume(e){

}