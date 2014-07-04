(function ($) {
  $(document).ready(function(){
    $("nav ul li").click(function() {
      var $items = $("div.items");
      if ($(this).hasClass("active"))
      {
        $(this).removeClass("active");
        $items.css("display", "none");
        return;
      }

      $items.css("display", "block");

      $("nav ul li").removeClass("active");
      $(this).addClass("active");

      $("div.items div").removeClass("active");
      var index = $(this).data("index");
      $('div.items div[data-index="' + index + '"]').addClass('active');
    });

    $(".datepicker").datepicker({
      closeText: 'Fermer',
      prevText: 'Précédent',
      nextText: 'Suivant',
      currentText: 'Aujourd\'hui',
      monthNames: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
      monthNamesShort: ['Janv.', 'Févr.', 'Mars', 'Avril', 'Mai', 'Juin', 'Juil.', 'Août', 'Sept.', 'Oct.', 'Nov.', 'Déc.'],
      dayNames: ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'],
      dayNamesShort: ['Dim.', 'Lun.', 'Mar.', 'Mer.', 'Jeu.', 'Ven.', 'Sam.'],
      dayNamesMin: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
      weekHeader: 'Sem.',
      minDate: new Date(),
      dateFormat : "dd/mm/yy"
    });


    $("form").submit(function() {
      $(this).find(".row").removeClass("error");
      var bError = false;
      var $email, $lastname, $firstname, $phone, $date, $message;

      $email = $(this).find('input[name=email]');
      var email = getMail($email.val());
      if (email === ""){
        setTimeout(function() {$email.parent(".row").addClass("error");}, 0);
        bError = true;
      }

      $firstname = $(this).find('input[name=firstname]');
      var firstname = $firstname.val();
      if (firstname === ""){
        setTimeout(function() {$firstname.parent(".row").addClass("error");}, 0);
        bError = true;
      }

      if (bError)
        return false;

      $lastname = $(this).find('input[name=lastname]');
      $phone = $(this).find('input[name=phone]');
      $date = $(this).find('input[name=date]');
      $message = $(this).find('textarea[name=message]');

      // send it
      jaxIt($(this), email, $lastname.val(), firstname, $phone.val(), $date.val(), $message.val());

      return false;
    });
  });

  function jaxIt($form, email, lastname, firstname, phone, date, message) {
    $.ajax({
      type: "GET",
      url: "/contact/",
      data: {
        'email': email,
        'lastname': lastname,
        'firstname': firstname,
        'phone': phone,
        'date': date,
        'message': message
      },
      success: function (data) {
        $form.before("<p>" + data.result + "</p>").remove();
      }
    });
  }

  function getMail(m) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);

    if (!pattern.test(m))
      m = '';

    return m;
  }

})(jQuery);
