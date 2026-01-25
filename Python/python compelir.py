import { useState } from 'react';
import { Play, Trash2, Download } from 'lucide-react';

export default function PythonCompiler() {
  const [code, setCode] = useState(`# Welcome to Python Compiler
# Write your Python code here and click Run

def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

# Try some calculations
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")
`);
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);

  const runCode = async () => {
    setIsRunning(true);
    setOutput('Running...\n');

    try {
      // Using Pyodide (Python in WebAssembly)
      if (!window.pyodide) {
        setOutput('Loading Python environment...\n');
        window.pyodide = await loadPyodide();
      }

      // Capture stdout
      window.pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
`);

      // Run user code
      try {
        await window.pyodide.runPythonAsync(code);
        const stdout = window.pyodide.runPython('sys.stdout.getvalue()');
        setOutput(stdout || 'Code executed successfully (no output)');
      } catch (err) {
        setOutput(`Error:\n${err.message}`);
      }
    } catch (err) {
      setOutput(`Failed to load Python environment:\n${err.message}\n\nNote: This requires an internet connection to load Pyodide.`);
    }

    setIsRunning(false);
  };

  const loadPyodide = () => {
    return new Promise((resolve, reject) => {
      if (window.loadPyodide) {
        window.loadPyodide().then(resolve).catch(reject);
      } else {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/pyodide/v0.23.4/full/pyodide.js';
        script.onload = () => {
          window.loadPyodide().then(resolve).catch(reject);
        };
        script.onerror = () => reject(new Error('Failed to load Pyodide'));
        document.head.appendChild(script);
      }
    });
  };

  const clearCode = () => {
    setCode('# Write your Python code here\n\n');
    setOutput('');
  };

  const downloadCode = () => {
    const blob = new Blob([code], { type: 'text/x-python' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'script.py';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-7xl mx-auto">
        <div className="bg-white rounded-lg shadow-2xl overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6">
            <h1 className="text-3xl font-bold flex items-center gap-3">
              <span className="text-4xl">🐍</span>
              Python Compiler
            </h1>
            <p className="text-blue-100 mt-2">Write, run, and test Python code in your browser</p>
          </div>

          {/* Main Content */}
          <div className="grid lg:grid-cols-2 gap-6 p-6">
            {/* Code Editor */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold text-gray-800">Code Editor</h2>
                <div className="flex gap-2">
                  <button
                    onClick={downloadCode}
                    className="flex items-center gap-2 px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg transition-colors"
                  >
                    <Download size={18} />
                    Download
                  </button>
                  <button
                    onClick={clearCode}
                    className="flex items-center gap-2 px-4 py-2 bg-red-100 hover:bg-red-200 text-red-700 rounded-lg transition-colors"
                  >
                    <Trash2 size={18} />
                    Clear
                  </button>
                </div>
              </div>
              
              <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                className="w-full h-96 p-4 font-mono text-sm bg-gray-900 text-green-400 rounded-lg border-2 border-gray-700 focus:border-blue-500 focus:outline-none resize-none"
                spellCheck={false}
                placeholder="Write your Python code here..."
              />

              <button
                onClick={runCode}
                disabled={isRunning}
                className="w-full flex items-center justify-center gap-3 px-6 py-3 bg-gradient-to-r from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700 text-white font-semibold rounded-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg"
              >
                <Play size={20} fill="white" />
                {isRunning ? 'Running...' : 'Run Code'}
              </button>
            </div>

            {/* Output Panel */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-gray-800">Output</h2>
              
              <div className="w-full h-96 p-4 font-mono text-sm bg-gray-900 text-gray-100 rounded-lg border-2 border-gray-700 overflow-auto whitespace-pre-wrap">
                {output || 'Output will appear here after running the code...'}
              </div>

              {/* Info Panel */}
              <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
                <h3 className="font-semibold text-blue-900 mb-2">💡 Tips:</h3>
                <ul className="text-sm text-blue-800 space-y-1">
                  <li>• Use <code className="bg-blue-100 px-1 rounded">print()</code> to display output</li>
                  <li>• First run may take a moment to load Python</li>
                  <li>• Most standard library modules are available</li>
                  <li>• Errors will be displayed in the output panel</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="text-center mt-6 text-gray-600 text-sm">
          <p>Powered by Pyodide - Python compiled to WebAssembly</p>
        </div>
      </div>
    </div>
  );
}
import { useState } from 'react';
import { Play, Trash2, Download } from 'lucide-react';

export default function PythonCompiler() {
  const [code, setCode] = useState(`# Welcome to Python Compiler
# Write your Python code here and click Run

def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

# Try some calculations
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")
`);
  const [output, setOutput] = useState('');
  const [isRunning, setIsRunning] = useState(false);

  const runCode = async () => {
    setIsRunning(true);
    setOutput('Running...\n');

    try {
      // Using Pyodide (Python in WebAssembly)
      if (!window.pyodide) {
        setOutput('Loading Python environment...\n');
        window.pyodide = await loadPyodide();
      }

      // Capture stdout
      window.pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
`);

      // Run user code
      try {
        await window.pyodide.runPythonAsync(code);
        const stdout = window.pyodide.runPython('sys.stdout.getvalue()');
        setOutput(stdout || 'Code executed successfully (no output)');
      } catch (err) {
        setOutput(`Error:\n${err.message}`);
      }
    } catch (err) {
      setOutput(`Failed to load Python environment:\n${err.message}\n\nNote: This requires an internet connection to load Pyodide.`);
    }

    setIsRunning(false);
  };

  const loadPyodide = () => {
    return new Promise((resolve, reject) => {
      if (window.loadPyodide) {
        window.loadPyodide().then(resolve).catch(reject);
      } else {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/pyodide/v0.23.4/full/pyodide.js';
        script.onload = () => {
          window.loadPyodide().then(resolve).catch(reject);
        };
        script.onerror = () => reject(new Error('Failed to load Pyodide'));
        document.head.appendChild(script);
      }
    });
  };

  const clearCode = () => {
    setCode('# Write your Python code here\n\n');
    setOutput('');
  };

  const downloadCode = () => {
    const blob = new Blob([code], { type: 'text/x-python' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'script.py';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-7xl mx-auto">
        <div className="bg-white rounded-lg shadow-2xl overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6">
            <h1 className="text-3xl font-bold flex items-center gap-3">
              <span className="text-4xl">🐍</span>
              Python Compiler
            </h1>
            <p className="text-blue-100 mt-2">Write, run, and test Python code in your browser</p>
          </div>

          {/* Main Content */}
          <div className="grid lg:grid-cols-2 gap-6 p-6">
            {/* Code Editor */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold text-gray-800">Code Editor</h2>
                <div className="flex gap-2">
                  <button
                    onClick={downloadCode}
                    className="flex items-center gap-2 px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg transition-colors"
                  >
                    <Download size={18} />
                    Download
                  </button>
                  <button
                    onClick={clearCode}
                    className="flex items-center gap-2 px-4 py-2 bg-red-100 hover:bg-red-200 text-red-700 rounded-lg transition-colors"
                  >
                    <Trash2 size={18} />
                    Clear
                  </button>
                </div>
              </div>
              
              <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                className="w-full h-96 p-4 font-mono text-sm bg-gray-900 text-green-400 rounded-lg border-2 border-gray-700 focus:border-blue-500 focus:outline-none resize-none"
                spellCheck={false}
                placeholder="Write your Python code here..."
              />

              <button
                onClick={runCode}
                disabled={isRunning}
                className="w-full flex items-center justify-center gap-3 px-6 py-3 bg-gradient-to-r from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700 text-white font-semibold rounded-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg"
              >
                <Play size={20} fill="white" />
                {isRunning ? 'Running...' : 'Run Code'}
              </button>
            </div>

            {/* Output Panel */}
            <div className="space-y-4">
              <h2 className="text-xl font-semibold text-gray-800">Output</h2>
              
              <div className="w-full h-96 p-4 font-mono text-sm bg-gray-900 text-gray-100 rounded-lg border-2 border-gray-700 overflow-auto whitespace-pre-wrap">
                {output || 'Output will appear here after running the code...'}
              </div>

              {/* Info Panel */}
              <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
                <h3 className="font-semibold text-blue-900 mb-2">💡 Tips:</h3>
                <ul className="text-sm text-blue-800 space-y-1">
                  <li>• Use <code className="bg-blue-100 px-1 rounded">print()</code> to display output</li>
                  <li>• First run may take a moment to load Python</li>
                  <li>• Most standard library modules are available</li>
                  <li>• Errors will be displayed in the output panel</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="text-center mt-6 text-gray-600 text-sm">
          <p>Powered by Pyodide - Python compiled to WebAssembly</p>
        </div>
      </div>
    </div>
  );
}



