module.exports = function(grunt){
  // project global config
  var __config = {
    project:      'evasion',
    static_root:  'evasion/static',

    css_version: 3,
    js_version: 2
  };

  // paths
  var __opts = {
    path: {
      js:     __config.static_root + '/js',
      scss:   __config.static_root + '/scss',
      css:    __config.static_root + '/css',
      mincss: __config.static_root + '/css/min',
      out:    __config.static_root + '/min'
    }
  };

  require('load-grunt-tasks')(grunt);

  var path = require('path');

  // externalize uglify parameters, to allow dynamic key assigning for file path (js_version)
  var uglify_parameters = {
      dist: {
        files: {
        }
      },
      dev: {
        options: {
          beautify: true,
          mangle: false
        },
        files: {
        }
      }
    };

  var js_files = [
    path.join('!' + __opts.path.js, '**/*min.js'),
    path.join(__opts.path.js, 'lib/jquery-2.1.1.js'),
    path.join(__opts.path.js, 'lib/jquery-ui.1.11.0.js'),
    path.join(__opts.path.js, 'lib/jquery.jdidbox-0.1.0.js'),
    path.join(__opts.path.js, 'lib/**/*.js'),
    path.join(__opts.path.js, '*.js')
  ];

  uglify_parameters.dist.files
    ['evasion/static/min/evasion.' + __config['js_version'] + '.min.js'] = js_files;

  uglify_parameters.dev.files
    ['evasion/static/min/evasion.' + __config['js_version'] + '.dev.min.js'] = js_files;

  grunt.initConfig({
    jshint: {
      default: [
        path.join('!' + __opts.path.js, 'lib'),
        path.join(__opts.path.js, '*.js')
      ]
    },

    uglify: uglify_parameters,

    compass: {
      dist: {
        options: {
          sassDir:  __opts.path.scss,
          cssDir:   __opts.path.mincss,
          environment: 'production',
          outputStyle: 'compressed',
          assetCacheBuster: false,
          raw: "sass_options = {:cache => false}\n"
        }
      },
      dev: {
        options: {
          sassDir:  __opts.path.scss,
          cssDir:   __opts.path.css,
          environment: 'development',
          outputStyle: 'nested',
          assetCacheBuster: false,
          raw: "sass_options = {:cache => false}\n"
        }
      }
    },

    concat: {
      dist: {
        src: [path.join(__opts.path.scss, "lib/**/*.css"), path.join(__opts.path.mincss, "*.css")],
        dest: path.join(__opts.path.out, __config.project + "." + __config.css_version + ".min.css")
      },
      dev: {
        src: [path.join(__opts.path.scss, "lib/**/*.css"), path.join(__opts.path.css, "*.css")],
        dest: path.join(__opts.path.out, __config.project + "." + __config.css_version + ".dev.min.css")
      }
    },

    copy: {
      jqueryui: {
        expand: true,
        cwd: path.join(__opts.path.scss, "lib/jquery-ui-1.11.0-custom/"),
        src: ["images/*"],
        dest: __opts.path.out
      },
      jdidbox: {
        expand: true,
        cwd: path.join(__opts.path.scss, "lib/jquery.jdidbox-0.1.0/"),
        src: ["*png", "*gif"],
        dest: __opts.path.out
      }
    },

    watch: {
      css: {
        files: [path.join(__opts.path.scss, '**/*.scss')],
        tasks: ['compass:dev', 'concat:dev']
      },
      js: {
        files: [path.join(__opts.path.js, '*.js')],
        tasks: ['uglify:dev']
      },
      gruntfile: {
        files: ["Gruntfile.js"],
        tasks: ['jshint:default']
      }
    },

    clean: [
      __opts.path.mincss,
      __opts.path.out
    ]
  });

  grunt.registerTask('css',     ['compass', 'concat']);
  grunt.registerTask('js',      ['jshint:default', 'uglify']);

  grunt.registerTask('dist',    ['jshint:default', 'uglify:dist', 'compass:dist', 'concat:dist', 'copy']);
  grunt.registerTask('dev',     ['jshint:default', 'uglify:dev', 'compass:dev', 'concat:dev', 'copy']);

  grunt.registerTask('all',     ['dev', 'dist']);
  grunt.registerTask('default', 'all');
};