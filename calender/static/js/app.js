
document.addEventListener('DOMContentLoaded', function () {
  var selected_info = ""
  var calendarEl = document.getElementById('calendar');
  
  var calendar = new FullCalendar.Calendar(calendarEl, {

    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
    },
      // initialView: 'dayGridMonth',
      businessHours: true,
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

      // dateClick: function() {
      //   // alert('dayClick')
      //   $(".day").removeClass("none")
      // },

      // selectLongPressDelay:0,
      // views: {
      //   timeGridDay:{
      //     viewDidMount:function(date){
      //       // alert(date)
      //       console.log(date.view.currentStart)
      //     }
          
      //   }
      // },
      datesSet:function(date){
        $(".day").addClass('none')
        if(date.view.type == "timeGridDay"){
          console.log(date.view)
          $(".day").html(date.view.currentStart)
          $(".day").removeClass('none')
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
        start: selected_info.start,
        end: selected_info.end,
        allDay: true,
    });
  })

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