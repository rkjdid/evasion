module.exports = function(grunt){
  // project global config
  var __config = {
    project:      'evasion',
    static_root:  'evasion/static'
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

  grunt.initConfig({
    jshint: {
      default: [
        path.join('!' + __opts.path.js, 'lib'),
        path.join(__opts.path.js, '*.js')
      ]
    },

    uglify: {
      dist: {
        files: {
          'evasion/static/min/evasion.0.min.js': [
            path.join('!' + __opts.path.js, '**/*min.js'),

            path.join(__opts.path.js, 'lib/jquery-2.1.1.js'),
            path.join(__opts.path.js, 'lib/**/*.js'),
            path.join(__opts.path.js, '*.js')
          ]
        }
      },
      dev: {
        options: {
          beautify: true,
          mangle: false
        },
        files: {
          'evasion/static/min/evasion.0.dev.min.js': [
            path.join('!' + __opts.path.js, '**/*min.js'),

            path.join(__opts.path.js, 'lib/jquery-2.1.1.js'),
            path.join(__opts.path.js, 'lib/**/*.js'),
            path.join(__opts.path.js, '*.js')
          ]
        }
      }
    },

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
        src: [path.join(__opts.path.mincss, "*.css")],
        dest: path.join(__opts.path.out, __config.project + ".0.min.css")
      },
      dev: {
        src: [path.join(__opts.path.css, "*.css")],
        dest: path.join(__opts.path.out, __config.project + ".0.dev.min.css")
      }
    },

    watch: {
      css: {
        files: [path.join(__opts.path.scss, '**/*.scss')],
        tasks: ['css']
      },
      js: {
        files: [path.join(__opts.path.js, '*.js')],
        tasks: ['js']
      },
      gruntfile: {
        files: ["Gruntfile.js"],
        tasks: ['jshint']
      }
    }

  });

  grunt.registerTask('css',     ['compass', 'concat']);
  grunt.registerTask('js',      ['jshint', 'uglify']);

  grunt.registerTask('dist',    ['jshint', 'uglify:dist', 'compass:dist', 'concat:dist']);
  grunt.registerTask('dev',     ['jshint', 'uglify:dev', 'compass:dev', 'concat:dev']);

  grunt.registerTask('all',     ['dev', 'dist']);
  grunt.registerTask('default', 'all');
};