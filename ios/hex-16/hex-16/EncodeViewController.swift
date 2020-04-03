//
//  EncodeViewController.swift
//  hex-16
//
//  Created by Bimo on 2020-04-02.
//  Copyright © 2020 carleotn. All rights reserved.
//

import UIKit

class EncodeViewController: UIViewController {
    
    var hexcode: String?
    
    @IBOutlet weak var imageView: UIImageView!
    @IBAction func decodeButton(_ sender: UIButton) {
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        guard let hexcode = hexcode else {
            print("hexcode error")
            return
        }
        
        let url = URL(string: "http://10.0.0.105:5000/encode?hexcode=\(hexcode)")!
        
        URLSession.shared.dataTask(with: url) { data, response, error in
            guard let data = data, error == nil else {
                return
            }
            
            DispatchQueue.main.async() {
                self.imageView.image = UIImage(data: data)
            }
        }.resume()
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
