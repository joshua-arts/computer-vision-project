//
//  DecodeViewController.swift
//  hex-16
//
//  Created by Bimo on 2020-04-02.
//  Copyright © 2020 carleotn. All rights reserved.
//

import UIKit

class DecodeViewController: UIViewController {
    
    var hexImage: UIImage?

    @IBOutlet weak var outputLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        guard let hexImage = hexImage else {
            return
        }
        
        let boundary = UUID().uuidString
        var request = URLRequest(url: URL(string: "http://10.0.0.105:5000/")!)
        request.httpMethod = "POST"
        request.setValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")
        
        var data = Data();
        
        data.append("\r\n--\(boundary)\r\n".data(using: .utf8)!)
        data.append("Content-Disposition: form-data; name=\"image\"; filename=\"hex.png\"\r\n".data(using: .utf8)!)
        data.append("Content-Type: image/png\r\n\r\n".data(using: .utf8)!)
        data.append(hexImage.pngData()!)
        data.append("\r\n--\(boundary)--\r\n".data(using: .utf8)!)
        
        URLSession.shared.uploadTask(with: request, from: data) { data, response, error in
            guard let data = data, error == nil else {
                return
            }
            
            let hexcode = String(data: data, encoding: .utf8);
            
            DispatchQueue.main.async() {
                self.outputLabel.text = hexcode
            }
        }.resume()
    }
}
