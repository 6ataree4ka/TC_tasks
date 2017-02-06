using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CaseSelector
{
    class CaseSelector
    {
        static void Main(string[] args)
        {
            string filePath = "";
            int caseNumber = 10;

            do
            {
                Console.WriteLine("Enter file path: ");
                string inputFilePath = Console.ReadLine().Trim();
                if (System.IO.File.Exists(inputFilePath))
                {
                    filePath = inputFilePath;
                }
                else
                {
                    Console.WriteLine("'{0}' file doesn't exist.", inputFilePath);
                }
            }
            while (filePath == "");

            Console.WriteLine("Enter required number of cases (default = 10): ");
            bool converted = Int32.TryParse(Console.ReadLine(), out caseNumber);
            if (!converted || caseNumber < 1)
            {
                caseNumber = 10;
            }

            string resPath = SelectCases(filePath, caseNumber);
            if (resPath != null)
            {
                Console.WriteLine("File with required number of cases is placed at {0}", resPath);
            }
            Console.ReadLine();
        }

        static string SelectCases(string file, int num = 10)
        {
            string[] lines = System.IO.File.ReadAllLines(file, Encoding.UTF8);
            if (lines.Length - 1 < num)
            {
                Console.WriteLine("The number of required cases is more than number cases in original file.");
                return null;
            }
            else
            {
                // num + 1 to reserve the first element for table head.
                string[] resArray = new string[num + 1];

                // Select random indices from original array with file strings.
                Random random = new Random();
                List<int> indices = new List<int>();
                while (indices.Count < num)
                {
                    int index = random.Next(1, lines.Length);
                    if (indices.Count == 0 || !indices.Contains(index))
                    {
                        indices.Add(index);
                    }
                }

                for (int i = 0; i < indices.Count; i++)
                {
                    int randomIndex = indices[i];
                    resArray[i + 1] = lines[randomIndex];
                }

                // Get original array without selected to the result file elements.
                string[] originalModified = lines.Except(resArray).ToArray();

                // Add table head.
                resArray[0] = lines[0];

                // Write to result file.
                string extension = System.IO.Path.GetExtension(file);
                string resFilePath = file.Replace(extension, "_res" + extension);
                System.IO.File.WriteAllLines(file.Replace(extension, "_res" + extension), resArray);

                // Modify original file.
                System.IO.File.WriteAllLines(file, originalModified, Encoding.UTF8);
                return resFilePath;
            }
        }
    }
}
