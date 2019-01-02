
        window.onload=function () {
            var link_concepts=document.getElementsByClassName("scrollspy-example")[0]
            var the_width=window.getComputedStyle(link_concepts).width

            var link_cards=document.getElementsByClassName("link_cards")
            for(var j=0;j<link_cards.length;j++){
                link_cards[j].style.width=(parseInt(the_width)/3.4).toString()+"px"
            }
            var link_concepts_cards=document.getElementsByClassName("link_concepts_cards")
            for(var i=0;i<link_concepts_cards.length;i++){
                link_concepts_cards[i].style.width=(parseInt(the_width)/3*link_cards.length).toString()+"px";
            }


            var expanded=false
            var expand=document.getElementById("expand")
            expand.onclick=function () {
                console.log(111);
                var box1=document.getElementsByClassName("main_concept")[0]
                var box2=document.getElementsByClassName("link_concepts")[0]
                var box3=document.getElementsByClassName("scrollspy-example")[0]
                if(expanded){
                    box1.style.height="500px"
                    box2.style.height="200px"
                    box3.style.height="200px"
                    expanded=false
                }
                else{
                    box1.style.height="350px"
                    box2.style.height="350px"
                    box3.style.height="350px"
                    expanded=true
                }
            }

            var scrollclick2=document.getElementById("not_avtive")
            scrollclick2.setAttribute("class","nav-link")

            var scrollclick=document.getElementById("link_name_menu").children[1]
            scrollclick.setAttribute("class","nav-link active")

            var button_move_left=document.getElementsByClassName("button_move_left")[0]
            var button_move_right=document.getElementsByClassName("button_move_right")[0]

            button_move_right.onmouseover=function () {
                var menu=this.nextElementSibling.nextElementSibling
                var childcount=menu.children.length
                var child_example=menu.children[0]
                if(childcount>3){
                    var onelength=window.getComputedStyle(child_example).width
                    onelength=parseInt(onelength)+parseInt(window.getComputedStyle(child_example).marginLeft)
                    var length=((childcount-3)*onelength+20).toString()+"px";
                    menu.style.transform="translateX(-"+length+")"
                }
            }
            button_move_left.onmouseover=function () {
                var menu=this.nextElementSibling
                menu.style.transform="translateX(0)"
            }
            var main_concept=document.getElementsByClassName("main_concept")[0]
            main_expended=false
            view_btn.onclick=function () {
                var spy=document.getElementById("spy")
                var linked_card=document.getElementById("linked_card")
                if(main_expended){
                    main_concept.style.transform="translate(0,0)"
                    spy.style.opacity="1"
                    linked_card.style.opacity="1"
                    main_expended=false
                }
                else{
                    main_concept.style.transform="translate(120px,120px)"
                    spy.style.opacity="0"
                    linked_card.style.opacity="0"
                    main_expended=true
                }
            }


            var is_open=false
            var view_reverse=document.getElementById("view_reverse")
            view_reverse.onclick=function () {
                var icon=this.children[0]
                var p=document.getElementsByClassName("flip-card-front")[0]
                var main_concept_body=document.getElementsByClassName("main_concept_body")[0]
                var inner=document.getElementsByClassName("flip-card-inner")[0]
                if(is_open){
                    icon.setAttribute("class","fas fa-toggle-off")
                    p.innerHTML=document.getElementsByClassName("flip-card-back")[0].innerHTML
                    p.setAttribute("style","text-align: left;font-size:15px")
                    main_concept_body.onmouseover=function(){

                    }
                    main_concept_body.onmouseout=function(){

                    }
                    is_open=false
                }
                else{
                    icon.setAttribute("class","fas fa-toggle-on")
                    p.innerHTML=main_concept.children[0].childNodes[0].textContent
                    is_open=true
                    main_concept_body.onmouseover=function(){
                        inner.style.transform="rotateY(180deg)"
                    }
                    main_concept_body.onmouseout=function(){
                        inner.style.transform="rotateY(0)"
                    }
                    p.setAttribute("style","text-align: center; font-size:35px")
                }
            }
        }