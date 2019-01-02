window.onload=function () {
            var link_concepts=document.getElementsByClassName("some_tags")[0]
            var the_width=window.getComputedStyle(link_concepts).width

            var link_cards=document.getElementsByClassName("link_cards")
            for(var j=0;j<link_cards.length;j++){
                link_cards[j].style.width=(parseInt(the_width)/3.4).toString()+"px"
                console.log(link_cards[j].style.width);
            }
            var link_concepts_cards=document.getElementsByClassName("link_concepts_cards")
            for(var i=0;i<link_concepts_cards.length;i++){
                link_concepts_cards[i].style.width=(parseInt(the_width)/3*link_cards.length/4.1).toString()+"px";
            }


            var button_move_left=document.getElementsByClassName("button_move_left")
            var button_move_right=document.getElementsByClassName("button_move_right")
            for(i=0;i<button_move_left.length;i++){
                button_move_right[i].onmouseover=function () {
                var menu=this.parentElement.nextElementSibling
                console.log(menu);
                    menu.style.transform="translateX(-"+(parseInt(the_width)-20)+"px)"
                }

                button_move_left[i].onmouseover=function () {
                   var menu=this.parentElement.nextElementSibling
                    menu.style.transform="translateX(0)"
                }
            }

        }
        $(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Initialize popover component
$(function () {
  $('[data-toggle="popover"]').popover()
})