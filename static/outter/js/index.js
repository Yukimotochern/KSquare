
var menu=document.getElementById("menu")
var current_instruct=document.getElementById("box_adv_1")
for(var i=0;i<menu.children.length;i++){
    var li=document.getElementById("menu_"+(i+1))
    li.onmouseover=function () {
        var box=document.getElementById("box_"+this.id)
        var boxs=document.getElementsByClassName("tag_instruct")
        current_instruct.style.display='none'
        box.style.display="block"
        current_instruct=box
        var menu_img=document.getElementsByClassName("menu_img")
        for(var j=0;j<menu_img.length;j++){
            menu_img[j].style.backgroundColor="skyblue"
        }
        this.children[0].style.backgroundColor="blue"
    }
}

var box2=document.getElementById("box2_menu")
var current_adv=document.getElementById("box_adv_1")
document.getElementById("adv_1").style.transform="scaleY(2)"
for(i=0;i<box2.children.length;i++){
    box2.children[i].children[0].onclick=function () {
        var dox=document.getElementById("box_"+this.id)
        if(current_adv==dox){
            return
        }
        current_adv.style.display="none"
        dox.style.display="block"
        current_adv=dox
        for(i=0;i<box2.children.length;i++){
            box2.children[i].children[0].style.transform="scaleY(1)"
        }
        this.style.transform="scaleY(2)"
    }
}
document.getElementById("to-left").onclick=function(){
    if(current_adv.id=="box_adv_1"){
        adv_4.click()
    }
    else if(current_adv.id=="box_adv_2"){
        adv_1.click()
    }
    else if(current_adv.id=="box_adv_3"){
        adv_2.click()
    }
    else if(current_adv.id=="box_adv_4"){
        adv_3.click()
    }
}
document.getElementById("to-right").onclick=function(){
    if(current_adv.id=="box_adv_1"){
        adv_2.click()
    }
    else if(current_adv.id=="box_adv_2"){
        adv_3.click()
    }
    else if(current_adv.id=="box_adv_3"){
        adv_4.click()
    }
    else if(current_adv.id=="box_adv_4"){
        adv_1.click()
    }
}
window.onload= function () {
    var scroll=document.getElementsByClassName("scroll")[0];//ie不兼容，换成id会成功
    var panel=document.getElementsByClassName("panel");//ie不兼容，换成id会成功

    var clientH=window.innerHeight;
    scroll.style.height=clientH+"px";
    for(var i=0;i<panel.length;i++){
        panel[i].style.height=clientH+"px";
    }
    /*下面是关于鼠标滚动*/
    var inputC=document.getElementsByTagName("input");
    var wheel= function (event) {
        var delta=0;
        if(!event)//for ie
            event=window.event;
        if(event.wheelDelta){//ie,opera
            delta=event.wheelDelta/120;
        }else if(event.detail){
            delta=-event.detail/3;
        }
        if(delta){
            handle(delta,inputC);
        }
        if(event.preventDefault)
            event.preventDefault();
        event.returnValue=false;
    };
    if(window.addEventListener){
        window.addEventListener('DOMMouseScroll',wheel,false);
    }
    window.onmousewheel=wheel;
};
function handle(delta,arr) {
    var num;
    for(var i=0;i<arr.length;i++){//得到当前checked元素的下标
        if(arr[i].checked){
            num=i;
        }
    }
    if(delta>0 && num>0){//向上滚动
        num--;
        arr[num].checked=true;
    }else if(delta<0 && num<4){//向下滚动
        num++;
        arr[num].checked=true;
    }
}

var expend_icons=document.getElementsByClassName("expend_icon")
for(var m=0;m<expend_icons.length;m++){
    expend_icons[m].onmouseover=function () {
        var mv=document.getElementsByClassName("mouseover-display")
        for(var k=0;k<mv.length;k++){
            mv[k].style.display="block"
        }
        for(var n=0;n<expend_icons.length;n++){
            expend_icons[n].style.display="none"
        }
    }
}

var box4_instruct_li=document.getElementsByClassName("box4_instruct_li")
for(m=0;m<box4_instruct_li.length;m++){
    box4_instruct_li[m].onmouseover=function () {
        var instruct_img=document.getElementsByClassName("box4_img")[0].children
        for(var k=0;k<instruct_img.length;k++){
            instruct_img[k].style.display="none"
        }
        document.getElementById(this.id+"_img").style.display="block"
        console.log(document.getElementById(this.id + "_img"));
    }
}


!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof exports?module.exports=a:a(jQuery)}(function(a){function b(b){var g=b||window.event,h=i.call(arguments,1),j=0,l=0,m=0,n=0,o=0,p=0;if(b=a.event.fix(g),b.type="mousewheel","detail"in g&&(m=-1*g.detail),"wheelDelta"in g&&(m=g.wheelDelta),"wheelDeltaY"in g&&(m=g.wheelDeltaY),"wheelDeltaX"in g&&(l=-1*g.wheelDeltaX),"axis"in g&&g.axis===g.HORIZONTAL_AXIS&&(l=-1*m,m=0),j=0===m?l:m,"deltaY"in g&&(m=-1*g.deltaY,j=m),"deltaX"in g&&(l=g.deltaX,0===m&&(j=-1*l)),0!==m||0!==l){if(1===g.deltaMode){var q=a.data(this,"mousewheel-line-height");j*=q,m*=q,l*=q}else if(2===g.deltaMode){var r=a.data(this,"mousewheel-page-height");j*=r,m*=r,l*=r}if(n=Math.max(Math.abs(m),Math.abs(l)),(!f||f>n)&&(f=n,d(g,n)&&(f/=40)),d(g,n)&&(j/=40,l/=40,m/=40),j=Math[j>=1?"floor":"ceil"](j/f),l=Math[l>=1?"floor":"ceil"](l/f),m=Math[m>=1?"floor":"ceil"](m/f),k.settings.normalizeOffset&&this.getBoundingClientRect){var s=this.getBoundingClientRect();o=b.clientX-s.left,p=b.clientY-s.top}return b.deltaX=l,b.deltaY=m,b.deltaFactor=f,b.offsetX=o,b.offsetY=p,b.deltaMode=0,h.unshift(b,j,l,m),e&&clearTimeout(e),e=setTimeout(c,200),(a.event.dispatch||a.event.handle).apply(this,h)}}function c(){f=null}function d(a,b){return k.settings.adjustOldDeltas&&"mousewheel"===a.type&&b%120===0}var e,f,g=["wheel","mousewheel","DOMMouseScroll","MozMousePixelScroll"],h="onwheel"in document||document.documentMode>=9?["wheel"]:["mousewheel","DomMouseScroll","MozMousePixelScroll"],i=Array.prototype.slice;if(a.event.fixHooks)for(var j=g.length;j;)a.event.fixHooks[g[--j]]=a.event.mouseHooks;var k=a.event.special.mousewheel={version:"3.1.12",setup:function(){if(this.addEventListener)for(var c=h.length;c;)this.addEventListener(h[--c],b,!1);else this.onmousewheel=b;a.data(this,"mousewheel-line-height",k.getLineHeight(this)),a.data(this,"mousewheel-page-height",k.getPageHeight(this))},teardown:function(){if(this.removeEventListener)for(var c=h.length;c;)this.removeEventListener(h[--c],b,!1);else this.onmousewheel=null;a.removeData(this,"mousewheel-line-height"),a.removeData(this,"mousewheel-page-height")},getLineHeight:function(b){var c=a(b),d=c["offsetParent"in a.fn?"offsetParent":"parent"]();return d.length||(d=a("body")),parseInt(d.css("fontSize"),10)||parseInt(c.css("fontSize"),10)||16},getPageHeight:function(b){return a(b).height()},settings:{adjustOldDeltas:!0,normalizeOffset:!0}};a.fn.extend({mousewheel:function(a){return a?this.bind("mousewheel",a):this.trigger("mousewheel")},unmousewheel:function(a){return this.unbind("mousewheel",a)}})});
	$(function(){
		var i=0;
		var $btn = $('.section-btn li'),
			$wrap = $('.section-wrap'),
			$arrow = $('.arrow');
		function up(){i++;if(i==$btn.length){i=0};}
		function down(){i--;if(i<0){i=$btn.length-1};}
		function run(){
			$btn.eq(i).addClass('on').siblings().removeClass('on');
			$wrap.attr("class","section-wrap").addClass(function() { return "put-section-"+i; }).find('.section').eq(i).find('.title').addClass('active');
		};
		$btn.each(function(index) {
			$(this).click(function(){
				i=index;
				run();
			})
		});
		/*翻页按钮点击*/
		$arrow.one('click',go);
		function go(){
			up();run();
			setTimeout(function(){$arrow.one('click',go)},1000)
		};
		$wrap.one('mousewheel',mouse_);
		function mouse_(event){
			if(event.deltaY<0) {up()}
			else{down()}
			run();
			setTimeout(function(){$wrap.one('mousewheel',mouse_)},1000)
		};
		/*响应键盘上下键*/
		$(document).one('keydown',k);
		function k(event){
			var e=event||window.event;
			var key=e.keyCode||e.which||e.charCode;
			switch(key)	{
				case 38: down();run();
				break;
				case 40: up();run();
				break;
			};
			setTimeout(function(){$(document).one('keydown',k)},1000);
		}
	});

	window.onload= function () {
            var scroll=document.getElementsByClassName("scroll")[0];//ie不兼容，换成id会成功
            var panel=document.getElementsByClassName("panel");//ie不兼容，换成id会成功

            var clientH=window.innerHeight;
            scroll.style.height=clientH+"px";
            for(var i=0;i<panel.length;i++){
                panel[i].style.height=clientH+"px";
            }
            /*下面是关于鼠标滚动*/
            var inputC=document.getElementsByTagName("input");
            var wheel= function (event) {
                var delta=0;
                if(!event)//for ie
                    event=window.event;
                if(event.wheelDelta){//ie,opera
                    delta=event.wheelDelta/120;
                }else if(event.detail){
                    delta=-event.detail/3;
                }
                if(delta){
                    handle(delta,inputC);
                }
                if(event.preventDefault)
                    event.preventDefault();
                event.returnValue=false;
            };
            if(window.addEventListener){
                window.addEventListener('DOMMouseScroll',wheel,false);
            }
            window.onmousewheel=wheel;
        };
        function handle(delta,arr) {
            var num;
            for(var i=0;i<arr.length;i++){//得到当前checked元素的下标
                if(arr[i].checked){
                    num=i;
                }
            }
            if(delta>0 && num>0){//向上滚动
                num--;
                arr[num].checked=true;
            }else if(delta<0 && num<4){//向下滚动
                num++;
                arr[num].checked=true;
            }
        }
        var public0=document.getElementById("public");
        public0.onmouseover=function () {
            document.getElementById("private").style.display="none"
            document.getElementsByClassName("public_instruct")[0].style.display="block"
            document.getElementsByClassName("public_img")[0].style.display="block"
        }
        public0.onmouseout=function () {
            document.getElementById("private").style.display="block"
            document.getElementsByClassName("public_instruct")[0].style.display="none"
            document.getElementsByClassName("public_img")[0].style.display="none"
        }
        var private0=document.getElementById("private")
        private0.onmouseover=function () {
            document.getElementById("public").style.display="none"
            document.getElementsByClassName("private_img")[0].style.display="block"
            document.getElementsByClassName("private_instruct")[0].style.display="block"

        }
        private0.onmouseout=function () {
            document.getElementById("public").style.display="block"
            document.getElementsByClassName("private_instruct")[0].style.display="none"
            document.getElementsByClassName("private_img")[0].style.display="none"
        }