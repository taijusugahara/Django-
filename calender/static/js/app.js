
document.addEventListener('DOMContentLoaded', function () {
  var selected_info = ""
  var calendarEl = document.getElementById('calendar');
  var now = new Date();
  var h = now.getHours();
  console.log(h)
  var calendar = new FullCalendar.Calendar(calendarEl, {

    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
    },
      // initialView: 'dayGridMonth',
      // businessHours: true,
      contentHeight: 'auto',
      navLinks: true,
      // locale: 'ja',
      locale: 'ja',
                buttonText: {
                    prev:     '<',
                    next:     '>',
                    prevYear: '<<',
                    nextYear: '>>',
                    today:    '今日',
                    month:    '月',
                    week:     '週',
                    day:      '日',
                    list:     '一覧',
                },
        allDayText: '終日',

        // slotMinTime: "12:00:00",
        scrollTime: "12:00:00",
        

      // dateClick: function() {
      //   // alert('dayClick')
      //   $(".day").removeClass("none")
      // },

      // selectLongPressDelay:0,
      allDayDidMount:function(){
        console.log("xxxxx")
      },
      views: {
        dayGridMonth:{
          dayMaxEvents:2,
        }
      },
      datesSet:function(date){
        $(".day").addClass('none')
        if(date.view.type == "timeGridDay"){
          
          console.log(date.view)
          $(".day").html(date.view.currentStart)
          $(".day").removeClass('none')
          console.log($(".fc-timegrid-slot").eq(18).offset().top)//30分単位
          var scroll_hour = h * 2
          var scroll_height = $(".fc-timegrid-slot-label").eq(18).offset().top
          // var scroll_height = $(".fc-timegrid-slot-label").eq(scroll_hour).offset().top
          $(window).scrollTop(scroll_height);
        }
      },
      eventClick:function (event) {
        console.log(event)
      },
      selectable: true,
        select: function (info) {
          selected_info = info
            // alert("selected " + info.startStr + " to " + info.endStr);
          //   const eventName = prompt("イベントを入力してください");
          //   if (eventName) {
          //     // イベントの追加
          //     calendar.addEvent({
          //         title: eventName,
          //         start: info.start,
          //         end: info.end,
          //         allDay: true,
          //     });
          // }
        // $("#button").on("click",function(){
        //       calendar.addEvent({
        //           title: "dammy",
        //           start: info.start,
        //           end: info.end,
        //           allDay: true,
        //       });
        // })

        },
        
  });

 

  // end-start
  $("#button").on("click",function(){
    console.log(selected_info.start)
    console.log(selected_info.end)
    calendar.addEvent({
        title: selected_info.start,
        start : selected_info.start,
        end: selected_info.start

        // start: selected_info.start,
        // end: selected_info.end,
        // allDay: true,
    });
  })

  function setScrollTime() {
    console.log(15)
    // setTimeout(
      calendar.scrollToTime(200)
    // )
    
    calendar.setOption('scrollTime', '04:00:00')
    // console.log(calendar.getOption('scrollTime'))
  }

  
  // $("#button").on("click",function(){
  //             calendar.addEvent({
  //                 title: "dammy",
  //                 start: info.start,
  //                 end: info.end,
  //                 allDay: true,
  //             });
  //       })

  calendar.render();
  
});