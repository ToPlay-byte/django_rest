const path = require('path');
const HTMLWebapckPlugin = require('html-webpack-plugin');
const HtmlWebpackRootPlugin = require('html-webpack-root-plugin-fixxed');
const MiniCSSExtractPlugih = require('mini-css-extract-plugin')
const { ProvidePlugin } = require('webpack')

 
module.exports = (env) => {

    const isDev = env.mode === 'development'
    const static_path = env.static_path ?? 'http://127.0.0.1:8000/static/'

    config = {
        mode: env.mode ?? 'development',
        entry: path.resolve(__dirname, 'src', 'index.jsx'),
        output: {
            path: path.resolve(__dirname, 'dist', 'js'),
            filename: '[name].js',
            publicPath: static_path,
            clean: true
        },
        module: {
            rules: [
                {
                    test: /\.scss/i,
                    exclude: /node_modules/i,
                    use: [
                        isDev ? 'style-loader': MiniCSSExtractPlugih.loader,
                        'style-loader',
                        'css-loader',
                        'sass-loader'
                    ],
                },
                {
                    test: /\.jsx?/i,
                    exclude: /node_modules/i,
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: [
                                '@babel/preset-env',
                                ['@babel/preset-react', {
                                    runtime: isDev ? 'automatic': 'classic'
                                }],

                            ]
                        }
                    }
                }
            ]
        },
        plugins: [
            !isDev && new MiniCSSExtractPlugih(
                {
                    filename: 'css/[name].[content].css',
                    chunkFilename: 'css/[name].[content].css'
                }
            ),
            new ProvidePlugin({
                React: 'react'
            })
        ],
        resolve: {
            extensions: ['.scss', '.jsx', '.js'],
            alias: {
                '@': path.resolve(__dirname, 'src')
            }
        }
        
    }

    return config
};