import ROOT
import os
import sys
#from samples.samples import *
from CMS_lumi import CMS_lumi
from variables import *
from sample import *
import copy
import json
import numpy as np


ROOT.gROOT.SetBatch()

#input dataset 
dataset = ["W_to_2Jets_Ele","W_to_2Jets_Mu","Top_W_minus_Lepton_2Q","W_to_2Jets_Mu","TT_Dileptonic_2024","TT_Semilep_2024","tWb_Signal_4FS_T","tWb_Signal_4FS_T_bar"]

#dataset = ["tWb_Signal_4FS_T"]

#Run3 

lumi = 124 #fb
blind = True


for d in dataset:
    if hasattr(sample_dict[d],"components"):
        components = sample_dict[d].components
    else:
        components = [sample_dict[d]]

#Folder of the data and Histo counts


folder = "/eos/user/f/fconfort/NanoAOD_outputs/Condor_file/"


#Creation of the dictionary for the signal and bkg 
infile = {"Signal" : [], "Bkg": []}
insample = {"Signal" : [], "Bkg": []}
Count = {"Signal" : [], "Bkg": []}




for dat in dataset:
    d = sample_dict[dat]
    #
    if hasattr(d, "components"):
        s_list = d.components
    else:
        s_list = [d]
    for s in s_list:    
        if "TBbarQ" in s.label or "TbarBQ" in s.label:
            #print(s.label)
            infile["Signal"].append(ROOT.TFile.Open(folder+"tWb_Analysis_filesnew"+s.label+"/"+s.label+"_histo.root"))       
            insample["Signal"].append(s)
            Count["Signal"].append(ROOT.TFile.Open(folder+"tWb_Analysis_countnew"+s.label+"/"+s.label+"_count.root"))
        elif "TT_Semilep_2024" in s.label or "TT_Dilep_2024" in s.label or "Top_W_minus_Lepton_2Q" or "Top_W_minus_2Lepton" or "W_to_2Jets_Mu":
            #print(s.label)
            infile["Bkg"].append(ROOT.TFile.Open(folder+"tWb_Analysis_filesnew"+s.label+"/"+s.label+"_histo.root"))
            insample["Bkg"].append(s)
            Count["Bkg"].append(ROOT.TFile.Open(folder+"tWb_Analysis_countnew"+s.label+"/"+s.label+"_count.root"))
        

#print(len(infile["Signal"]))
#print(len(insample["Signal"]))


for v in vars:
    for r in regions.keys():
        #Bisogna vedere se la combinazione delle variabili e all'intenrod del file root di apertura:
        exists = False
        for f,s,c in zip(infile["Signal"],insample["Signal"],Count["Signal"]):
            events_dir = f.Get("Events")

            if not events_dir:
                continue
            # Controllo se esiste l'instogramma.
            histo_name = v._name + r 
            if events_dir.Get(histo_name):
                exists = True
                print(histo_name)
                break
        if not exists:
            continue
        #print()


        
        ROOT.gROOT.SetStyle("Plain")
        ROOT.gStyle.SetOptStat(0)
        ROOT.TH1.SetDefaultSumw2()
        stack = ROOT.THStack(v._name+r,v._name+r)
        leg_stack = ROOT.TLegend(0.45,0.88,0.9,0.71)
        leg_stack.SetNColumns(2)
        leg_stack.SetFillColor(0)
        leg_stack.SetFillStyle(0)
        leg_stack.SetTextFont(42)
        leg_stack.SetBorderSize(0)
        leg_stack.SetTextSize(0.03)

        #Part for the legend in the stack plot
        l =[]

        #===============================================================
        #======================Signal===================================
        #===============================================================

        h_signal_total = None


        for i, (f,s,c) in enumerate(zip(infile["Signal"],insample["Signal"],Count["Signal"])):
            events_dir = f.Get("Events")
            if not events_dir:
                print(f"Events directory not found in {f.GetName()}")
                continue

            hist_name = v._name + r
            tmp_hist = events_dir.Get(hist_name)
            if not tmp_hist:
                print(f"Histogram {hist_name} not found in file {f.GetName()}")
                continue

            tmp = tmp_hist.Clone()
            tmp.SetDirectory(0)
            tmp_signal = tmp_hist.Clone()

            h_count = c.Get("Events/nEvents")
            n_total = h_count.Integral()

            #Scale at the luminosity of the data
            tmp.Scale(s.sigma*(10**3)*0.32*lumi/(n_total))
            tmp_signal.Scale(0.45*(10**3)*lumi/(n_total))


            for ibin in range(1, tmp.GetNbinsX() + 1):
                width = tmp.GetXaxis().GetBinWidth(ibin)
                tmp.SetBinContent(ibin, tmp.GetBinContent(ibin) / width)
                tmp.SetBinError(ibin, tmp.GetBinError(ibin) / width)

            for ibin in range(1, tmp_signal.GetNbinsX() + 1):
                width = tmp_signal.GetXaxis().GetBinWidth(ibin)
                tmp_signal.SetBinContent(ibin, tmp_signal.GetBinContent(ibin) / width)
                tmp_signal.SetBinError(ibin, tmp_signal.GetBinError(ibin) / width)

            



            #tmp.Rebin(2)
            tmp.GetXaxis().SetTitle(v._title)
            tmp.SetLineColor(0)
            tmp.SetLineWidth(0)
            tmp.SetFillColor(s.color)
            tmp.SetName(s.leglabel)
            tmp.SetTitle("")
            #tmp.Rebin(2)
            #tmp_signal.Rebin(2)
            stack.Add(tmp)
            if s.leglabel not in l:
                l.append(s.leglabel)    
                leg_stack.AddEntry(tmp,s.leglabel, "f")


            if h_signal_total is None:
                h_signal_total = tmp_signal.Clone("h_signal_total")
                h_signal_total.SetDirectory(0)
            else:
                h_signal_total.Add(tmp_signal)

        
        if h_signal_total:
            h_signal_total.Scale(100)  # <-- moltiplica tutto il segnale per 1000
            h_signal_total.SetLineColor(ROOT.kBlue)
            h_signal_total.SetLineWidth(3)
            h_signal_total.SetLineStyle(1)  # 1=continua, 2=tratteggiata
            h_signal_total.SetFillStyle(0)
            h_signal_total.SetTitle("")
            leg_stack.AddEntry(h_signal_total, "(ST_{b,q} + ST_{q,b})  #times 100", "l")




        #========================================================   
        #======================bkg===============================   
        #========================================================

        hists_bkg = {}


        for i, (f,s,c) in enumerate(zip(infile["Bkg"],insample["Bkg"],Count["Bkg"])):
            events_dir = f.Get("Events")
            if not events_dir:
                print(f"Events directory not found in {f.GetName()}")
                continue

            hist_name = v._name + r
            tmp_hist = events_dir.Get(hist_name)
            if not tmp_hist:
                print(f"Histogram {hist_name} not found in file {f.GetName()}")
                continue

            tmp = tmp_hist.Clone()
            tmp.SetDirectory(0)
            
            h_count = c.Get("Events/nEvents")
            n_total = h_count.Integral()

            #Scale at the luminosity of the data
            tmp.Scale(s.sigma*(10**3)*lumi/(n_total))
            
            
            for ibin in range(1, tmp.GetNbinsX() + 1):
                width = tmp.GetXaxis().GetBinWidth(ibin)
                tmp.SetBinContent(ibin, tmp.GetBinContent(ibin) / width)
                tmp.SetBinError(ibin, tmp.GetBinError(ibin) / width)
            
            #tmp.Rebin(0)
            tmp.GetXaxis().SetTitle(v._title)
            tmp.SetLineColor(0)
            tmp.SetLineWidth(0)
            tmp.SetLineColor(ROOT.kBlack)
            tmp.SetFillColor(s.color)
            tmp.SetName(s.leglabel)
            tmp.SetTitle("")
            #tmp.Rebin(2)
            #stack.Add(tmp)
            #if s.leglabel not in l:
                #l.append(s.leglabel)    
                #leg_stack.AddEntry(tmp,s.leglabel, "f")
            
            
            
            if s.leglabel not in hists_bkg:
                hists_bkg[s.leglabel] = tmp.Clone()
                hists_bkg[s.leglabel].SetFillColor(s.color)
                hists_bkg[s.leglabel].SetLineColor(ROOT.kBlack)
                hists_bkg[s.leglabel].SetLineWidth(1)
            else:
                hists_bkg[s.leglabel].Add(tmp)
 
        for leglabel, hist in hists_bkg.items():
            stack.Add(hist)
            leg_stack.AddEntry(hist, leglabel, "f")
        

    

        #Draw part
        canvasname = "canvas_" + v._name + "_" + r
        
        output_dir = "/eos/user/f/fconfort/tWb_Stack_Plots_new"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        #outfile_prefix = "./"

        # Canvas più ampia (1000x800)
        c1 = ROOT.TCanvas(canvasname, "c1", 1000, 700)
        c1.SetFillColor(0)
        c1.SetBorderSize(1)
        c1.SetFrameFillStyle(0)
        c1.SetFrameBorderMode(0)

        # Margini più bilanciati
        c1.SetLeftMargin(0.14)
        c1.SetRightMargin(0.05)
        c1.SetTopMargin(0.08)
        c1.SetBottomMargin(0.14)

        # Tick sugli assi
        c1.SetTickx(1)
        c1.SetTicky(1)

        # -----------------------
        # Scale settings
        # -----------------------
        if not blind and not v._MConly:
            maximum = max(stack.GetMaximum(), h_data.GetMaximum())
        else:
            maximum = stack.GetMaximum()
        
        """
        if len(h_sign) != 0 and h_sign[-1].GetMinimum() != 0:
            minimum = h_sign[-1].GetMinimum()
        elif stack.GetMinimum() != 0:
            minimum = stack.GetMinimum() * 1e-1
        else:
            minimum = 1e-1
        """
        minimum = 1e-1


        # Choose scale
        logscale = False
        if logscale:
            stack.SetMaximum(maximum * 100)
            stack.SetMinimum(minimum)
        else:
            stack.SetMaximum(maximum * 1.5)
            stack.SetMinimum(minimum * 0.8)

        # -----------------------
        # Draw stack and components
        # -----------------------
        stack.SetTitle("")
        
        
        #stack_total.SetLineColor(ROOT.kBlack)
        #stack.SetLineWidth(2)
        #stack.SetFillStyle(0)  # solo contorno
        #stack.Draw("HIST SAME")


        stack.Draw("HIST")
        if h_signal_total:
            h_signal_total.Draw("HIST SAME")


        """
        for hist in hists_bkg.values():
            outline = hist.Clone(hist.GetName() + "_outline")
            outline.SetFillStyle(0)
            outline.SetLineColor(ROOT.kBlack)
            outline.SetLineWidth(2)
            outline.Draw("HIST SAME")
        """


        # Axis labels (più spazio e font più grandi)
        stack.GetXaxis().SetTitle(v._title)
        stack.GetYaxis().SetTitle("Events / bin width")
        stack.GetXaxis().SetTitleSize(0.055)
        stack.GetYaxis().SetTitleSize(0.055)
        stack.GetXaxis().SetLabelSize(0.05)
        stack.GetYaxis().SetLabelSize(0.05)
        stack.GetXaxis().SetTitleOffset(1.2)
        stack.GetYaxis().SetTitleOffset(1.4)

        # Stat uncertainty band
        h_err = stack.GetStack().Last().Clone("h_err")
        h_err.SetTitle("")
        h_err.SetLineWidth(0)
        h_err.SetFillStyle(3154)
        h_err.SetMarkerSize(0)
        h_err.SetFillColor(ROOT.kGray + 2)
        leg_stack.AddEntry(h_err, "Stat. Unc.", "f")

        h_err.Draw("e2 same")

        """
        # Draw signals
        for h in h_sign:
            h.Draw("HIST SAME")
        """


        # Legend più alta e spostata leggermente a destra
        leg_stack.SetX1NDC(0.75)
        leg_stack.SetY1NDC(0.60)
        leg_stack.SetX2NDC(0.98)
        leg_stack.SetY2NDC(0.88)
        leg_stack.SetTextSize(0.035)
        leg_stack.Draw("same")

        # CMS + lumi
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        lumi_sqrtS = f"{lumi} fb^{{-1}}  (13.6 TeV)"
        iPos = 10
        CMS_lumi(c1, lumi_sqrtS, iPos, "")
        
        
        region_label = ROOT.TLatex()
        region_label.SetNDC()              # coordinate normalizzate
        region_label.SetTextFont(62)       # font bold CMS style
        region_label.SetTextSize(0.05)     # grandezza del testo
        region_label.SetTextAlign(13)      # sinistra-alto
        region_label.DrawLatex(0.22, 0.96, f"#bf{{{r}}}")  # posizione leggermente più alta e più a destra
        



        # Log scale opzionale
        if logscale:
            c1.SetLogy()

        # Redraw & save
        c1.Update()
        c1.RedrawAxis()

        for ext in ["png", "pdf", "C"]:
            c1.Print(os.path.join(output_dir, canvasname + "." + ext))


