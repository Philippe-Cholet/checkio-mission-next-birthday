//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {

        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'next_birthday',
                js: 'nextBirthday',
            }
        });
        io.start();
    }
);
