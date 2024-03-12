#!/usr/bin/node

const fs = require('fs');

const [, , sourceFile1, sourceFile2, destFile] = process.argv;

const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');

const concatenatedContent = content1 + '\n' + content2;

fs.writeFileSync(destFile, concatenatedContent);

console.log('Concatenation complete.');
