/*product区域的js功能*/
var product_part1="<div class='row'>"+
                        "<h2>${ name }</h2>"+
                    "</div>"+
                    "<div class='row product_bg'>"+
                        "<div class='product_left'>"+
                            "<pre>${ content }</pre>"+
                        "</div>"+
                        "<div class='product_right'>"+
                            "<img src='${ img_url }'/>"+
                        "</div>"+
                    "</div>";
var product_part2="<div class='row'>"+
                        "<h2>${ name }</h2>"+
                        "<pre>${ content }</pre>"+
                    "</div>";
var product_part3="<div class='row product_bg'>"+
                        "<div class='product_left'>"+
                            "<div class='product_up'>"+
                                "<h5>>${ purpore }</h5>"+
                            "</div>"+
                            "<div class='product_down'>"+
                                "<pre>${ content }</pre>"+
                            "</div>"+
                        "</div>"+
                        "<div class='product_right'>"+
                            "<img src='${ img_url }'/>"+
                        "</div>"+
                    "</div>";
var product_part4="<div class='row part4'>"+
                        "<h2>>${ name }</h2>"+
                        "<div class='part4_left'>"+
                            "<pre>${ content }</pre>"+
                        "</div>"+
                        "<div class='part4_right'>"+
                            "<img src='${ img_url }'/>"+
                        "</div>"+
                    "</div>";
$.template("product_part1",  product_part1 );
$.template("product_part2",  product_part2 );
$.template("product_part3",  product_part3 );
$.template("product_part4",  product_part4 );

function product_post(url,cls){
    $.ajax({
            type: 'POST',
            url:url ,
            dataType:'json',
            data: {cls:cls},
            success:function(msg){
                var part=msg.part1;
                console.log(part.length);
                console.log(part[0].name);
                $('.coordination').empty();
                for(var i=0;i<msg.part1.length;i++){
                    var part1=msg.part1[i];
                    $.tmpl( "product_part1",part1).appendTo( ".coordination" );
                }
                for(var i=0;i<msg.part2.length;i++){
                    var part2=msg.part2[i];
                    $.tmpl( "product_part2",part2).appendTo( ".coordination" );
                }
                for(var i=0;i<msg.part3.length;i++){
                    var part3=msg.part3[i];
                    $.tmpl( "product_part3",part3).appendTo( ".coordination" );
                }
                for(var i=0;i<msg.part4.length;i++){
                    var part4=msg.part4[i];
                    $.tmpl( "product_part4",part4).appendTo( ".coordination" );
                }
            }
        });
}

/*solutions区域的js功能*/
var solutions_part1="<div class='row solutions_part1'>"+
                        "<div class='part1_left'>"+
                            "<h3>${ name }</h3>"+
                            "<pre>${ content }</pre>"+
                        "</div>"+
                        "<div class='part1_right'>"+
                            "<img src='${ img_url }'/>"+
                        "</div>"+
                    "</div>";
var solutions_part2="<div class='row solutions_part2'>"+
                        "<h3>${ name }</h3>"+
                        "<pre>${ content }</pre>"+
                    "</div>";
var solutions_part3_content="<div class='row solutions_part3'></div>";
var solutions_part3="<div class='part3_half'>"+
                        "<div class='part3_left'>"+
                            "<img src='${ img_url }'/>"+
                        "</div>"+
                        "<div class='part3_right'>"+
                            "<pre>${ content }</pre>"+
                        "</div>"+
                    "</div>";
$.template("solutions_part1", solutions_part1);
$.template("solutions_part2", solutions_part2);
$.template("solutions_part3_content", solutions_part3_content);
$.template("solutions_part3", solutions_part3);
function solutions_post(url,cls){
    $.ajax({
            type: 'POST',
            url:url ,
            dataType:'json',
            data: {cls:cls},
            success:function(msg){
                $('.solutions').empty();
                console.log(msg)
                for(var i=0;i<msg.part1.length;i++){
                    var part1=msg.part1[i];
                    $.tmpl( "solutions_part1",part1).appendTo( ".solutions" );
                }
                for(var i=0;i<msg.part2.length;i++){
                    var part2=msg.part2[i];
                    $.tmpl( "solutions_part2",part2).appendTo( ".solutions" );
                }
                $.tmpl( "solutions_part3_content",part3).appendTo( ".solutions" );
                for(var i=0;i<msg.part3.length;i++){
                    var part3=msg.part3[i];
                    $.tmpl( "solutions_part3",part3).appendTo( ".solutions_part3" );
                }
            }
        });
}

$(document).ready(function(){
    //product区域
    $("#coordination_summary").click(function(){
        product_post('','概述')
    });
    $("#coordination_function").click(function(){
        product_post('','功能')
    });
    $("#coordination_technology").click(function(){
        product_post('','技术')
    });
    //solutions区域
    $("#solutions_summary").click(function(){
        solutions_post('','概述')
    });
    $("#solutions_function").click(function(){
        solutions_post('','功能')
    });
    $("#solutions_frame").click(function(){
        solutions_post('','架构')
    });
    $("#solutions_characteristic").click(function(){
        solutions_post('','特点')
    });
    $("#solutions_technology").click(function(){
        solutions_post('','技术')
    });
    $("#solutions_service").click(function(){
        solutions_post('','服务')
    });

});
